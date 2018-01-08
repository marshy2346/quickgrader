import os
import shutil
import zipfile
from pathlib import Path

def unzip(src, dst):
   """
   Unzips a file from src to dst.

   :param src: source zipfile path
   :param dst: destination path
   """
   ref = zipfile.ZipFile(src, 'r')
   ref.extractall(dst)
   ref.close()

def get_tmpfile_name(directory):
    """
    Returns a generic temporary file name expected for all output files.
    :param directory:
    """
    return '{}-tmp.txt'.format("".join(directory.split()))

def remove_ext(file):
    """
    Removes extension from filename

    :param file: file with extension
    """
    return os.path.splitext(file)[0]

def get_ext(path):
    """
    Returns the extension of a file or path to a file.

    :param path: path to file
    """
    fn, ext = os.path.splitext(path)
    return ext

def home():
    """
    Returns home directory path
    """
    return str(Path.home())

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

