import os
import shutil

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

# TODO: make this useful for quickgrader v2.0
def get_working_directory():
    """
    Moves all zip files in DIRECTORY and moves them to
    WORKING_DIRECTORY_PATH. All new unzipped folder paths
    will be returned.
    """
    path = DIRECTORY
    directories = []

    # removing working directory folder if it exists
    print(""" Initializing working directory """)
    if os.path.isdir(WORKING_DIRECTORY_PATH):
            print(""" Working directory exists... """)
            print(""" Deleting working_directory...  """)
            shutil.rmtree(WORKING_DIRECTORY_PATH)
            print(""" Finished.  \n\n""")

    # make new working directory folder
    os.mkdir(WORKING_DIRECTORY_PATH)

    # unzipping and flattening each directory and moving to working dir
    for directory in os.listdir(path):
        current_path = os.path.join(path, directory)
        output_path = os.path.join(
            WORKING_DIRECTORY_PATH, remove_ext(get_uin(directory))
        )

        if current_path.endswith('zip'):
            unzip(current_path, output_path)
            flatdir(output_path)

            # copy driver to folder
            shutil.copyfile(DRIVER, os.path.join(output_path, DRIVER))

            # add directory
            directories.append(output_path)
        else:
            print(""" {} not detected as zip file. """.format(current_path))

    print(""" Initialization complete. """)

    return directories
def get_working_directory():
