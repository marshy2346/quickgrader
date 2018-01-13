import os
from configparser import ConfigParser

from utils.fs import (
    home
)


class SettingsManager:
    def __init__(self):
        self.default_editor = '' 
        self.keymap = {
            'New Project': 'Ctrl+I',
            'Open Project': 'Ctrl+O',
            'Save': 'Ctrl+S',
            'Next Submission': 'Ctrl+Right',
            'Previous Submission': 'Ctrl+Left',
            'Plugins': 'Ctrl+P',
            'Exit': 'Ctrl+Q',
            'Export': 'Ctrl+E'
        }

    def save(self):
        config = ConfigParser()
        config.add_section('editor')
        config.set('editor', 'default_editor', self.default_editor)

        config.add_section('keymap')
        config.set('keymap', 'New Project', self.keymap['New Project'])
        config.set('keymap', 'Open Project', self.keymap['Open Project'])
        config.set('keymap', 'Save', self.keymap['Save'])
        config.set('keymap', 'Next Submission', self.keymap['Next Submission'])
        config.set('keymap', 'Previous Submission', self.keymap['Previous Submission'])
        config.set('keymap', 'Plugins', self.keymap['Plugins'])
        config.set('keymap', 'Exit', self.keymap['Exit'])
        config.set('keymap', 'Export', self.keymap['Export'])

        with open(os.path.join(home(), '.qgsettings'), 'w') as f:
            config.write(f)

    def load(self):
        path = os.path.join(home(), '.qgsettings')
        if os.path.isfile(path):
            config = ConfigParser()
            config.read(path)
            self.default_editor = config.get('editor', 'default_editor')
            self.keymap = config['keymap']
