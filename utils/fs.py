import os
import sys
import shutil
import subprocess 
import zipfile
from pathlib import (
    Path
)

def unzip(src, dst):
   """ 
   Unzips a file from src to dst.

   :param src: source zipfile path
   :param dst: destination path
   """
   ref = zipfile.ZipFile(src, 'r')
   ref.extractall(dst)
   ref.close()

def open_file(file_path, program_path=None):
    # TODO: needs to be tested
    """
    Opens file specified by path with default program unless otherwise
    specified.

    :param str file_path: path to file
    :param str program_path: path to program 
    """
    if program_path is not None and program_path is not '':
        subprocess.Popen([program_path, file_path])
    else:
        if sys.platform.startswith('darwin'):
            subprocess.Popen(['open', file_path])
        elif os.name == 'nt':
            os.startfile(file_path)
        elif os.name == 'posix':
            subprocess.Popen(('xdg-open', file_path))



def is_hidden_file(file):
    """
    Checks if file specified is a hidden file (starts with '.')

    :param str file: name of file or path to file
    :returns: True if hidden file, False otherwise
    """
    base = os.path.basename(file)
    return base.startswith('.')       


def is_directory(path):
    """
    Checks if path is a valid directory
    
    :param str path: path to directory
    :returns: True if valid, False otherwise
    """
    return path != None and os.path.isdir(path)

def is_file(path):
    """
    Checks if path is a valid file 
    
    :param str path: path to file 
    :returns: True if valid, False otherwise
    """
    return path != None and os.path.isfile(path)

def overwrite(path):
    """
    Deletes file or directory and creates a new empty file or directory.

    :param path: the path to file or directory
    """
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.mkdir(path)
    elif os.path.isfile(path):
        fd = open(path, 'w')
        fd.close()

def home():
    """
    Returns home directory path
    """
    return str(Path.home())

def get_ext(path):
    """
    Returns the extension of a file or path to a file.

    :param path: path to file
    """
    fn, ext = os.path.splitext(path)
    return ext

def flatdir(dir):
    """
    Moves all files up to the root directory.

    :param dir: directory to flatten
    """
    full_path = os.path.abspath(dir)

    for root, dirs, files in os.walk(full_path, topdown=False):
        for file in files:
            fpath = os.path.join(root, file)
            new_path = os.path.join(full_path, file)
            shutil.move(fpath, new_path)

        for dir in dirs:
            dirpath = os.path.join(root, dir)
            os.rmdir(dirpath)

    return dirs

def remove_ext(file):
    """
    Removes extension from filename

    :param file: file with extension
    """
    return os.path.splitext(file)[0]
