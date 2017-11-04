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

class Mode:
    CONSOLE = "CONSOLE"
    GUI = "GUI"

MODE = Mode.CONSOLE

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
    """
    Very naive implementation to get the uin from the filename

    :param filename: the student file
    :return: the uin
    """
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

def init_tempfiles():
    """
    Initializes all temporary files used.

    files
    ------
    comments
    error
    """
    # TODO: saved path

    # removing comments file if it exists
    if os.path.isfile(COMMENTS_PATH):
        error_prompt(""" {} exists.\n\n """.format(COMMENTS_PATH))
        os.remove(COMMENTS_PATH)
    # removing error file if it exists
    if os.path.isfile(ERROR_PATH):
        os.remove(ERROR_PATH)

    # create error file
    fd = open(ERROR_PATH, 'w', encoding='utf-8')
    fd.close()

    # create comments file
    fd1 = open(COMMENTS_PATH, 'w', newline='')
    fd.close()

    if os.path.isfile(SAVED_PATH):
        with open(SAVED_PATH, 'r', encoding='utf-8') as fd:
            CURRENT_INDEX = int(fd.readline())

@contextmanager
def cd(newdir):
    """
    Changes to directory

    :param newdir: directory to change to
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

    :param args: the arguments to run
    :param stdin: optional stdin
    :param shell: optional shell
    """
    proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=stdin,
        shell=shell
    )

    out, err = proc.communicate()

    # bytes -> utf-8
    return out.decode('utf-8'), err.decode('utf-8')

def write_error(name, error):
    """
    Writes error to error file and increments error counter

    :param name: name to describe what student had error
    :param error: error output
    """
    global global_nerrors
    global_nerrors += 1

    print(""" Error found in {}. """.format(name))
    print(""" Writing to error file... """)

    with open(ERROR_PATH, 'a', encoding='utf-8') as errfd:
        errfd.write("{}\n".format(name))

    print(""" Complete. \n\n""")

def run_diff(name):
    """
    Runs a program that shows differences in the expected output and the actual output.

    Windows:
        FC
    Unix:
        vimdiff

    :param name: the name of the file to run the difference on
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
    """
    Used to write a comment to a CSV file.

    :param name: name to describe the student
    :param comment: the comment to be added
    """
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

    :param directory: the path to the directory to compile the driver
    :param driver: the path to the driver
    :return: stdout, stderr
    """
    with cd(directory):
        stdout, stderr = Popen_communicate([JAVAC_COMMAND, driver])
    return stdout, stderr

def run_driver(directory, driver, input=None):
    """
    Runs the driver and returns stdout and stderr

    :param directory: the path to the directory to run driver
    :param driver: the path to the driver
    :param input: optional input to the program
    :return: stdout, stderr
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

    :param message: the message to display
    """
    print(""" \n{} """.format(message))
    choice = input(""" Continue? (y/n) """)
    if choice.lower() != 'y':
        print(""" Bye. """)
        sys.exit(0)

def user_prompt(message, response_cb):
    print(""" \n{} """.format(message))
    response = input(""":> """)
    return response_cb(response)

def print_gui_prompt():
    print(""" ==========================================""")
    print(""" You are in GUI Mode. """)
    print(""" ==========================================""")
    print(""" Additional Commands: """)
    print(""" --------------------------------------------------------------------------------- """)
    print(""" r <filename>.java (run)     - compiles and runs java file """)
    print(""" e                 (error)   - log to error and go to next student """)
    print(""" n                 (next)    - next student """)
    print(""" c <message>       (comment) - add a comment for the student in comments.csv """)
    print(""" h                 (help)    - to display this prompt again """)
    print(""" --------------------------------------------------------------------------------- """)
    print(""" [Note]: All commands from your interpreter program should work. """)
    print("""                                        """)

def commandline(directory_base, directory):
    INTERACTING = True
    while INTERACTING:
        args = input(":> ").strip()

        args_lower = args.lower()
        args_split = [s for s in args.split(' ')]

        if args_lower == 'error' or args_lower == 'e':
            return '', 'compile or run error' # write skipped to error file
        elif 'quit' in args_lower or args_lower == 'q':
            sys.exit(0)
        elif args_lower == 'n' or args_lower == 'next':
            # this is really hacky but its so no error is written out
            return '', ''
        elif args_lower[0] == 'c' or args_lower[:6] == 'comment':
            if len(args_split) < 2:
                print("Forgot to add a comment...")
                print("ex: $ c add comment here")
                continue
            add_comment(directory_base, args[2:])
            continue

        elif args_lower == 'h' or args_lower == 'help':
            print_gui_prompt()
            continue

        if args_split[0].lower() == 'run' or args_split[0].lower() == 'r':
            if len(args_split) < 2:
                args_split.append(DRIVER)

            c_out, c_err = compile_driver(directory, args_split[1])
            if c_err != '':
                print(c_err)
            r_out, r_err = run_driver(directory, args_split[1])
            if r_err != '':
                print(r_err)
            else:
                print(r_out)
        else:
            with cd(directory):
                out, err = Popen_communicate([s for s in args.split(' ')])

                if err != '':
                    print(err)
                else:
                    print(out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui-mode", help="""
        puts the program in gui mode which only compiles code and then walks through each submission allowing
        the user to run whichever program he wants.
    """, action="store_true")
    args = parser.parse_args()

    if args.gui_mode:
        MODE = Mode.GUI

    directories = get_working_directory()

    init_tempfiles()

    # show number of directories moved
    ndirs = len(directories)
    print(""" {} Directories moved. \n\n""".format(ndirs))

    if MODE == Mode.GUI:
        print_gui_prompt()

    for directory in directories:
        COMPILED = False
        RUN = False

        directory_base = os.path.basename(directory)

        if MODE == Mode.GUI:
                if os.name == 'nt':
                    args = ['dir']
                else:
                    args = ['ls']

                with cd(directory):
                    out, err = Popen_communicate(args)
                if err != '':
                    write_error(directory_base, err)
                else:
                    # prints out list of files
                    print(""" Files in {} """.format(directory))
                    print(""" ---------------------------""")
                    print(out)

                    # if the user enters skip then the program will log the student in error file
                    out, err = commandline(directory_base, directory)
                    print(err)

                    if err != '':
                        global_run_errors += 1
                        write_error(directory_base, err)

        elif MODE == Mode.CONSOLE:

            # Compilation Stage
            compile_out, compile_err = compile_driver(directory, DRIVER)
            if compile_err != '':
                global_compile_errors += 1

                write_error(directory_base, compile_err)
            else:
                COMPILED = True

            # Run Stage
            if COMPILED:

                if MODE == Mode.CONSOLE:
                    if os.path.isfile(INPUT_FILE):
                        with open(INPUT_FILE, 'r', encoding='utf-8') as inputfd:
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
                        with open(tmpfile_name, 'w', encoding='utf-8') as tmpfile:
                            tmpfile.write(run_out)

            if RUN:
                run_diff(directory)
                comment = input(""" Add a comment: """)
                add_comment(directory_base, comment)

    print(""" ---- Results ---- """)
    print(""" Errors: {} """.format(global_nerrors))
    print("""   Compile: {} """.format(global_compile_errors))
    print("""   Runtime: {} """.format(global_run_errors))

