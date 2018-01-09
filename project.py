import pickle
import shutil
import os
import re
from enum import Enum

import constants
from models.submission import Submission
from utils.fs import get_ext, overwrite, home, remove_ext, flatdir, unzip
from utils.parsing import get_uin
from ui.dialog import request_info, request_directory, show_warning, show_message

#TODO: clean up logic
#TODO: support more extensions
#TODO: rethink what happens when unsupported extension is found
#TODO: what happens if project_control_block save fails?

SUPPORTED_EXTS = ['.zip']

INVALID_NAME_MESSAGE = (
    'Project names must be larger than 3 characters'
    ' and contain only alphanumeric characters.'
)

INVALID_SOURCE_MESSAGE = (
    'Source must be a directory containing files with these'
    ' supported extensions ({}).'.format(','.join(SUPPORTED_EXTS))
)

INVALID_STATE_MESSAGE = (
    'The project is in an invalid state. This is probably due'
    ' to a corrupted or non-existent project file.'
)

PROJECT_EXISTS_MESSAGE = (
    'The requested project name already exists.'
    ' Would you like to overwrite it?'
)

class ProjectManagerState(Enum):
    NAME_VALID = 1
    NAME_INVALID = -1
    SOURCE_VALID = 2
    SOURCE_INVALID = -2
    PCB_STATE_VALID = 3
    PCB_STATE_INVALID = -3
    PCB_STATE_RECOVERY_SOURCE_VALID = 4
    PCB_STATE_RECOVERY_SOURCE_INVALID = -4
    UNINITIALIZED = -5 

class ProjectManager:
    PROJECT_CONTROL_BLOCK_FILENAME = '.qgproject'

    def __init__(self):
        self.state = ProjectManagerState.UNINITIALIZED
        self.project_control_block = {
            'path': '',
            'pcb_path': '',
            'submissions': [],
            'finished_submissions': [],
            'current_submission_index': 0,
        }

    def __reset(self):
        self.project_control_block['path'] = ''
        self.project_control_block['pcb_path'] = ''
        self.project_control_block['submissions'] = []
        self.project_control_block['finished_submissions'] = []
        self.project_control_block['current_subission_index'] = 0

    def __is_valid_source(self, source_path):
        self.state = ProjectManagerState.SOURCE_INVALID

        if source_path == None or not os.path.isdir(source_path):
            return False

        dirs = os.listdir(source_path)
        if len(dirs) == 0:
            return False

        for file in os.listdir(source_path):
            if get_ext(file) not in SUPPORTED_EXTS:
                return False

        self.state = ProjectManagerState.SOURCE_VALID
        return True

    def __is_valid_pcb_recovery_file(self, path):
        self.state = ProjectManagerState.PCB_STATE_RECOVERY_SOURCE_INVALID

        if path == None or not os.path.isfile(path) or os.path.basename(path) != ProjectManager.PROJECT_CONTROL_BLOCK_FILENAME:
            return False

        self.state = ProjectManagerState.PCB_STATE_RECOVERY_SOURCE_VALID
        return True

    def __is_valid_name(self, name):
        self.state = ProjectManagerState.NAME_INVALID

        if name == None or name == '':
            return False

        if len(name) < 3 or not re.match('^\w+$', name):
            return False

        self.state = ProjectManagerState.NAME_VALID
        return True


    def __try_control_block_recovery(self, directory_path):
        self.state = ProjectManagerState.PCB_STATE_INVALID

        for file in os.listdir(directory_path):
            full_path = os.path.join(directory_path, file)

            if self.__is_valid_pcb_recovery_file(full_path):
                with open(full_path, 'rb') as pcbfile:
                    try:
                        self.__reset()
                        self.project_control_block = pickle.load(pcbfile)
                        self.project_control_block['pcb_path'] = full_path
                    except pickle.UnpicklingError:
                        return False
                self.state = ProjectManagerState.PCB_STATE_VALID
                return True

        return False
   
    def __try_control_block_save(self):
        if self.state != ProjectManagerState.PCB_STATE_VALID:
            return False

        with open(self.project_control_block['pcb_path'], 'wb') as pcbfile:
            try:
                pickle.dump(self.project_control_block, pcbfile)
            except pickle.PicklingError:
                self.state = ProjectManagerState.PCB_STATE_INVALID
                return False

        return True

    def __handle_create_project_folder(self, qt_widget, name):
        if self.state != ProjectManagerState.NAME_VALID:
            return False

        project_path = os.path.join(constants.WORKSPACE_PATH, name)
        success = False

        if os.path.isdir(project_path):
            ok = show_warning(
                qt_widget,
                PROJECT_EXISTS_MESSAGE
            )
            if ok:
                overwrite(project_path)
                success = True
            else:
                success = False

        else:
            # TODO: does os.mkdir always succeed?
            os.mkdir(project_path)
            success = True

        return success

    def __handle_setup_project(self, qt_widget, name, source_directory):
        if self.state != ProjectManagerState.SOURCE_VALID:
            return False

        project_path = os.path.join(constants.WORKSPACE_PATH, name)

        self.__reset()
        self.project_control_block['path'] = project_path
        self.project_control_block['pcb_path'] = os.path.join(project_path, ProjectManager.PROJECT_CONTROL_BLOCK_FILENAME)

        for file in os.listdir(source_directory):
            current_path = os.path.join(source_directory, file)
            output_path = os.path.join(project_path, remove_ext(get_uin(file)))

            #TODO: add support for more file types and change this to account for that
            if get_ext(file) == '.zip':
                unzip(current_path, output_path)
                flatdir(output_path)

            self.project_control_block['submissions'].append(Submission(output_path))

        self.state = ProjectManagerState.PCB_STATE_VALID
        return self.__try_control_block_save()

    def __abort(self):
        if os.path.isdir(self.project_control_block['path']):
            shutil.rmtree(self.project_control_block['path'])

    def open(self, qt_widget):
        source_directory = ""
        valid_directory = False

        while source_directory != None and not valid_directory:
            source_directory = request_directory(qt_widget, 'Choose source directory', home())
            valid_directory = source_directory is not None and os.path.isdir(source_directory)

            if not valid_directory and source_directory != None:
                show_message(qt_widget, INVALID_SOURCE_MESSAGE)

        return self.__try_control_block_recovery(source_directory)


    def new(self, qt_widget):
        project_name = ""
        valid_name = False 

        while project_name != None and not valid_name:
            project_name = request_info(qt_widget, 'Project Name')
            valid_name = self.__is_valid_name(project_name)

            if not valid_name and project_name != None:
                show_message(qt_widget, INVALID_NAME_MESSAGE)

        if not self.__handle_create_project_folder(qt_widget, project_name):
            return False

        source_directory = ""
        valid_directory = False

        while source_directory != None and not valid_directory: 
            source_directory = request_directory(qt_widget, 'Choose source directory', home())
            valid_directory = self.__is_valid_source(source_directory)

            if not valid_directory and source_directory != None:
                show_message(qt_widget, INVALID_SOURCE_MESSAGE)

        if not valid_directory or not self.__handle_setup_project(qt_widget, project_name, source_directory):
            self.__abort()
            return False

        return True

    def save(self, qt_widget):
        if self.state != ProjectManagerState.PCB_STATE_VALID:
            return

        success = self.__try_control_block_save()

        if not success:
            show_message(qt_widget, INVALID_STATE_MESSAGE)

    def current_submission(self):
        if self.state != ProjectManagerState.PCB_STATE_VALID:
            return None

        return self.project_control_block['submissions'][self.project_control_block['current_submission_index']]

    def next_submission(self):
        submission_count = len(self.project_control_block['submissions']) - 1
        self.project_control_block['current_submission_index'] = (self.project_control_block['current_submission_index'] + 1) % submission_count

    def prev_submission(self):
        submission_count = len(self.project_control_block['submissions']) - 1
        self.project_control_block['current_submission_index'] = (self.project_control_block['current_submission_index'] - 1) % submission_count
                                        

