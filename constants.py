VERSION = "2.0"

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
