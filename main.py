import os
import shutil
import sys
import subprocess
import zipfile
import csv
import re
import argparse
from contextlib import contextmanager

from config import *

"""
This program gets all zip files in a specified folder, compiles and runs 
specified driver and finally runs a 'diff' command to see the difference
between what was expected and what the output actually was.
"""

WORKING_DIRECTORY_PATH = "working_directory"
ERROR_PATH = "errors.txt"
COMMENTS_PATH = "comments.csv"
# TODO: Finish save feature
SAVED_PATH = "saved.txt"
CURRENT_INDEX = 0

global_nerrors = 0
global_compile_errors = 0
global_run_errors = 0

def get_uin(filename):
    uin = ""
    n = 0
    skip = True
    for c in filename:
        if n == 4:
            break
        if c.isdigit():
            if skip:
                skip = False
            else:
                uin += c
                n += 1
    if uin == "":
        return filename
    else:
        return uin

def remove_first_match(file, regex):
    #TODO: test this 
    stop_matching = False
    data = []
    with open(file, 'w') as f:
        for line in f: 
            m = re.match(regex, line) 
            if m and not stop_matching:
                stop_matching = True
            else:
                data.append(line)
        f.writelines(data)

def flatdir(dir):
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

def unzip(src, dst):
   ref = zipfile.ZipFile(src, 'r')
   ref.extractall(dst)
   ref.close()

def get_tmpfile_name(directory):
    return '{}-tmp.txt'.format("".join(directory.split()))

def remove_ext(file):
    """
    Removes extension from filename
    """
    return os.path.splitext(file)[0]

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

        unzip(current_path, output_path)
        flatdir(output_path)

        # copy driver to folder
        shutil.copyfile(DRIVER, os.path.join(output_path, DRIVER))

        # add directory 
        directories.append(output_path)

    print(""" Initialization complete. """)

    return directories

def init_tempfiles():
    # removing comments file if it exists
    if os.path.isfile(COMMENTS_PATH):
        error_prompt("""{} exists.\n\n """.format(COMMENTS_PATH)) 
        os.remove(COMMENTS_PATH)
    # removing error file if it exists
    if os.path.isfile(ERROR_PATH):
        os.remove(ERROR_PATH)

    # create error file
    fd = open(ERROR_PATH, 'w', encoding='ascii')
    fd.close()

    # create comments file
    fd1 = open(COMMENTS_PATH, 'w', newline='')
    fd.close()

    if os.path.isfile(SAVED_PATH):
        with open(SAVED_PATH, 'r', encoding='ascii') as fd:
            CURRENT_INDEX = int(fd.readline())

@contextmanager
def cd(newdir):
    """
    Changes to directory
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def Popen_communicate(args, stdin=None, shell=False):
    """
    Hooks into Popen io and returns stdout, stderr
    """
    proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=stdin,
        shell=shell
    )

    out, err = proc.communicate()

    # bytes -> ascii
    return out.decode('ascii'), err.decode('ascii')

def write_error(name, error):
    """
    Writes error to error file and increments error counter
    """
    global global_nerrors 
    global_nerrors += 1

    print(""" Error found in {}. """.format(name))
    print(""" Writing to error file... """)
    
    with open(ERROR_PATH, 'a', encoding='ascii') as errfd:
        errfd.write("{}\n".format(name))

    print(""" Complete. \n\n""")

def run_diff(name):
    """
    Runs the diff for two files 
    """
    tmp = get_tmpfile_name(name)
    print(""" Capturing diff for {}. """.format(name))
    if not os.path.isfile(tmp):
        error_prompt(""" {} file not found. """.format(tmp))
    if os.path.isfile(EXPECTED_OUTPUT_FILE):
        if os.name == 'nt':
            os.system("""FC {} {}""".format(EXPECTED_OUTPUT_FILE, tmp))
        else: 
            os.system("""vimdiff {} {}""".format(EXPECTED_OUTPUT_FILE, tmp))
    else:
        error_prompt(""" Expected output file not found. """)

def add_comment(name, comment):
    if not os.path.isfile(COMMENTS_PATH):
        error_prompt(""" Can't find comments file. """)
        sys.exit(-1)
    print(""" Writing comment for {}. \n""".format(name))
    with open(COMMENTS_PATH, 'a', newline='') as csvfile:
        cwriter = csv.writer(
            csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        cwriter.writerow([name, comment])
        print(""" Finished. """)

def compile_driver(directory, driver):
    """
    Compiles the driver and returns stdout and stderr
    """
    with cd(directory):
        stdout, stderr = Popen_communicate([JAVAC_COMMAND, driver])
    return stdout, stderr

def run_driver(directory, driver, input=None):
    """
    Runs the driver and returns stdout and stderr
    """
    with cd(directory):
        stdout, stderr = Popen_communicate(
            [JAVA_COMMAND, remove_ext(driver)],
            stdin=input
        ) 
    return stdout, stderr

def error_prompt(message):
    """
    Prints an error prompt
    """
    print("""\n\n {} """.format(message))
    choice = input(""" Continue? (y/n) """)
    if choice.lower() != 'y':
        print(""" Bye. """)
        sys.exit(0)


if __name__ == "__main__":
    directories = get_working_directory()

    init_tempfiles()

    # show number of directories moved
    ndirs = len(directories)
    print(""" {} Directories moved. \n\n""".format(ndirs))

    for directory in directories:
        COMPILED = False
        RUN = False

        directory_base = os.path.basename(directory)

        # Compilation Stage
        compile_out, compile_err = compile_driver(directory, DRIVER)            
        if compile_err != '':
            global_compile_errors += 1

            write_error(directory_base, compile_err) 
        else:
            COMPILED = True

        # Run Stage
        if COMPILED:
            if os.path.isfile(INPUT_FILE):
                with open(INPUT_FILE, 'r', encoding='ascii') as inputfd:
                    run_out, run_err = run_driver(directory, DRIVER, inputfd)
            else:
                error_prompt(""" Input file not found. """)
                run_out, run_err = run_driver(directory, DRIVER)

            if run_err != '':
                global_run_errors += 1

                write_error(directory_base, run_err)
            else:
                RUN = True
                # write output to temp file for diff
                tmpfile_name = get_tmpfile_name(directory)
                with open(tmpfile_name, 'w', encoding='ascii') as tmpfile:
                    tmpfile.write(run_out)

        if RUN:
            run_diff(directory)
            comment = input(""" Add a comment: """)
            add_comment(directory_base, comment)

    print(""" ---- Results ---- """)
    print(""" Errors: {} """.format(global_nerrors))
    print("""   Compile: {} """.format(global_compile_errors))
    print("""   Runtime: {} """.format(global_run_errors))

