import os
import shutil 
import pickle

from utils.fs import (
    is_directory,
    is_file
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

    def __abort(self):
        if os.path.isdir(self.state['project_path']):
            shutil.rmtree(self.state['project_path'])

    def __isvalid_statefile(self, path):
        return is_file(path) and os.path.basename(path) == ProjectManager.STATE_FILENAME

    def save(self):
        project_path = self.state['project_path']
        if not is_directory(project_path)
            return False 

        state_path = os.path.join(project_path, ProjectManager.STATE_FILENAME)
        with open(state_path, 'wb') as statefile:
            try:
                pickle.dump(self.state, statefile)
                return True
            except pickle.PicklingError:
                return False

    def load(self, directory_path):
        # TODO: handle possible invalid state
        if not is_directory(directory_path):
            return False

        for file in os.listdir(directory_path):
            full_path = os.path.join(directory_path, file)

            if self.__isvalid_statefile(full_path):
                with open(full_path, 'rb') as statefile:
                    self.__reset()
                    try:
                        self.state = pickle.load(statefile)
                        self.state['project_path'] = os.path.dirname(full_path)
                        return True
                    except pickle.UnpicklingError:
                        return False

    def get_current_submission(self):
        if len(self.state['submissions']) == 0:
            return None

        return self.state['submissions'][self.state['current_submission_index']]
      
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
