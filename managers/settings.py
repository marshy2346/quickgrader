import os
import pickle

from utils.fs import (
    home,
    is_file
)


SETTINGS_PATH = os.path.join(home(), '.qgsettings')
SETTING_TYPE_FILE = "FILE"
SETTING_TYPE_STRING = "STRING"


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
        self.plugins = {}

    def set_default_plugin_setting(self, plugin, setting, _type, value):
        if plugin not in self.plugins:
            self.plugins[plugin] = {}
            self.plugins[plugin][setting] = {'type': _type, 'value': value}
        elif setting not in self.plugins[plugin]:
            self.plugins[plugin][setting] = {'type': _type, 'value': value}
        else:
            return

    def get_plugin_settings(self, plugin_name):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name]
        return {}

    def save(self):
        with open(SETTINGS_PATH, 'wb') as settingsfile:
            dump = {
                'default_editor': self.default_editor,
                'keymap': self.keymap,
                'plugins': self.plugins
            }
            try:
                pickle.dump(dump, settingsfile)
                return True
            except pickle.PicklingError:
                return False

    def load(self):
        if os.path.isfile(SETTINGS_PATH):
            with open(SETTINGS_PATH, 'rb') as settingsfile:
                try:
                    dump = pickle.load(settingsfile)
                    self.default_editor = dump['default_editor']
                    self.keymap = dump['keymap']
                    self.plugins = dump['plugins']
                    return True
                except pickle.UnpicklingError:
                    return False
        return False
