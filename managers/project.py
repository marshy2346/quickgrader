import os
import json
import shutil
import pickle

from utils.fs import (
    is_directory,
    is_file,
    get_ext,
    remove_ext,
    flatdir,
    unzip
)
from utils.parsing import (
    get_uin
)
from models.submission import (
    Submission
)


class ProjectManager:

    STATE_FILENAME = '.qgproject'

    def __init__(self):
        self.state = {
            'project_path': None,
            'submissions': [],
            'finished_submissions': [],
            'current_submission_index': 0
        }

    def __reset(self):
        self.state['submissions'] = []
        self.state['finished_submissions'] = []
        self.state['current_submission_index'] = 0

    def __isvalid_statefile(self, path):
        return is_file(path) and os.path.basename(path) == ProjectManager.STATE_FILENAME

    def __isvalid_projectname(self, name):
        return name is not None and len(name) > 3

    def __isvalid_source(self, source_path):
        # TODO: determine more robust method for checking if source files are valid
        if is_directory(source_path):
            dirs = os.listdir(source_path)
            if len(dirs) == 0:
                return False

            return True
        else:
            return False

    def cleanup(self):
        if os.path.isdir(self.state['project_path']):
            shutil.rmtree(self.state['project_path'])

    def new(self, project_path, source_directory):
        if is_directory(project_path) and self.__isvalid_source(source_directory):
            self.__reset()
            self.state['project_path'] = project_path

            for file in os.listdir(source_directory):
                current_path = os.path.join(source_directory, file)
                output_path = os.path.join(project_path, remove_ext(get_uin(file)))

                # TODO: add support for more file types and change this to account for that
                if get_ext(file) == '.zip':
                    unzip(current_path, output_path)
                    flatdir(output_path)
                    self.state['submissions'].append(Submission(output_path))

            return self.save() and len(self.state['submissions']) > 0 and self.state['project_path'] != None
        else:
            return False

    def save(self):
        project_path = self.state['project_path']
        if is_directory(project_path):
            state_path = os.path.join(project_path, ProjectManager.STATE_FILENAME)
            with open(state_path, 'wb') as statefile:
                try:
                    pickle.dump(self.state, statefile)
                    return True
                except pickle.PicklingError:
                    return False
        else:
            return False

    def load(self, directory_path):
        # TODO: handle possible invalid state
        if is_directory(directory_path):
            for file in os.listdir(directory_path):
                full_path = os.path.join(directory_path, file)

                if self.__isvalid_statefile(full_path):
                    with open(full_path, 'rb') as statefile:
                        self.__reset()
                        try:
                            self.state = pickle.load(statefile)
                            return True
                        except pickle.UnpicklingError:
                            return False
        else:
            return False

    def is_project_loaded(self):
        submission = self.get_current_submission()
        return submission != None

    def get_current_submission(self):
        if len(self.state['submissions']) == 0:
            return None

        return self.state['submissions'][self.state['current_submission_index']]

    def get_submissions_json(self):
        json = []
        for submission in self.state['submissions']:
            if submission is not None:
                json.append(submission.get_json())
        return json

    def next_submission(self):
        if len(self.state['submissions']) == 0:
            return

        submission_count = len(self.state['submissions']) - 1
        current_index = self.state['current_submission_index']

        self.state['current_submission_index'] = (current_index + 1) % submission_count

    def prev_submission(self):
        if len(self.state['submissions']) == 0:
            return

        submission_count = len(self.state['submissions']) - 1
        current_index = self.state['current_submission_index']

        self.state['current_submission_index'] = (current_index - 1) % submission_count
