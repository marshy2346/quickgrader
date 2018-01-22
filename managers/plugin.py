import importlib
import glob
import sys
import os

from utils.dialog import (
    show_message
)


class Plugin:
    def __init__(self, path, ui_delegator):
        self.name = None
        self.module = None
        self.ui_delegator = ui_delegator

        mod_name = os.path.dirname(path)
        if sys.platform == "nt":
            mod_name = mod_name.replace('\\', '.')
        else:
            mod_name = mod_name.replace("/", '.')

        try:
            self.module = importlib.import_module(mod_name)
            self.name = mod_name[mod_name.index('.') + 1:len(mod_name)].capitalize()
        except ImportError:
            self.module = None

    def add_action(self, text, handler):
        self.ui_delegator.add_action(text, handler)

    def get_settings(self):
        manager = self.ui_delegator.delegate.settings_manager
        return manager.get_plugin_settings(self.name)

    def add_default_setting(self, setting, _type, default_value):
        manager = self.ui_delegator.delegate.settings_manager
        manager.set_default_plugin_setting(self.name, setting, _type, default_value)

    def show_message(self, message):
        show_message(self.ui_delegator.delegate, message)


class PluginManager:
    def __init__(self, ui_delegator):
        self.plugins = []
        self.__load_plugins(ui_delegator)

    def setup(self):
        for p in self.plugins:
            try:
                p.module.setup(p)
            except AttributeError:
                continue

    def __load_plugins(self, ui_delegator):
        for init_file in glob.glob("plugins/**/__init__.py"):
            p = Plugin(init_file, ui_delegator)
            self.plugins.append(p)

    def get_plugin(self, name):
        for p in self.plugins:
            if p.name == name:
                return p
        return None

