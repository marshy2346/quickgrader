import os
import subprocess 

def open_file(file_path, program_path=None):
    # TODO: needs to be tested
    """
    Opens file specified by path with default program unless otherwise
    specified.

    :param str file_path: path to file
    :param str program_path: path to program 
    """
    if program_path is not None:
        subprocess.Popen([program_path, file_path])
    else:
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', file_path))
        elif os.name == 'nt':
            os.startfile(file_path)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', file_path))

def is_hidden_file(file):
    """
    Checks if file specified is a hidden file (starts with '.')

    :param str file: name of file or path to file
    :returns: True if hidden file, False otherwise
    """
    base = os.path.basename(filename)
    return base.startswith('.')       
