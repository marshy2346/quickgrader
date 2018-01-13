import os
from utils.fs import (
    home
)

# TODO: move module-specific constants to module __init__.py

VERSION = "2.0"

SUPPORTED_EXTS = ['.zip']

DEFAULT_THEME = "default"

WORKSPACE_PATH = os.path.join(home(), "QuickGraderProjects")

MESSAGE_SETTINGS_EDITOR_HELP = (
    "Add the name of your preferred editor in the text field."
    " Leaving it blank or writing default will recover default settings."
    " If you get errors, add the full path to the executable."
)

MESSAGE_ABOUT = (
    "This project was created in order to facilitate grading student submissions from Canvas."
    "\n"
    "\n"
    "File bug reports and feature requests by visiting"
    "\n"
    "https://github.com/rayrase/quickgrader.git"
    "\n\n"
    "Created By Raisel Martinez | rayrase@github.com"
)

MESSAGE_INVALID_NAME = (
    'Project names must be larger than 3 characters'
    ' and contain only alphanumeric characters.'
)

MESSAGE_INVALID_SOURCE = (
    'Source must be a directory containing files with these'
    ' supported extensions ({}).'.format(','.join(SUPPORTED_EXTS))
)

MESSAGE_INVALID_STATE = (
    'The project is in an invalid state. This is probably due'
    ' to a corrupted or non-existent project file.'
)

MESSAGE_SAVE_ERROR = (
   "Saving was unsuccessful. Please try again."
)

MESSAGE_SAVE = (
    "Project successfully saved!"
)

MESSAGE_PROJECT_NOTLOADED = (
    "There is no loaded project. Open or create a new"
    " project by accessing the file menu."
)

MESSAGE_PROJECT_EXISTS = (
    'The requested project name already exists.'
    ' Would you like to overwrite it?'
)
