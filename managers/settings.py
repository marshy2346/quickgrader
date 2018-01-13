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
        config['keymap'] = self.keymap

        with open(os.path.join(home(), '.qgsettings'), 'w') as f:
            config.write(f)

    def load(self):
        path = os.path.join(home(), '.qgsettings')
        if os.path.isfile(path):
            config = ConfigParser()
            config.read(path)
            self.default_editor = config.get('editor', 'default_editor')
            self.keymap = config['keymap']
