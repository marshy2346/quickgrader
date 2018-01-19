import subprocess
import sys
import os
from contextlib import contextmanager

SETTING_INPUT_FILE = "Input File"
EXPECTED_OUTPUT_FILE = "Expected Output File"
COMPILE_ERR_FILENAME = "compile_err.txt"
RUNTIME_ERR_FILENAME = "run_err.txt"
COMPILE_OUT_FILENAME = "compile_out.txt"
RUNTIME_OUT_FILENAME = "run_out.txt"
COMPILE_TITLE = "Compilation"
RUNTIME_TITLE = "Runtime"


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def popen_communicate(args, stdin=None, shell=False):
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
    sys.stdout.write(out.decode('utf-8'))

    # bytes -> utf-8
    return out.decode('utf-8'), err.decode('utf-8')


def compile_and_run(filepath, settings, show_message, update):
    dir = os.path.dirname(filepath)
    filename = os.path.basename(filepath)

    if SETTING_INPUT_FILE in settings:
        stdin = settings[SETTING_INPUT_FILE]['value']
    else:
        stdin = None

    with cd(dir):
        out, err = popen_communicate(["javac", filename], stdin=stdin)
        if err != '':
            show_message(err)
            with open(COMPILE_ERR_FILENAME, 'w') as f:
                f.write(err)
            return

        out, err = popen_communicate(["java", os.path.splitext(filename)[0]], stdin=stdin)

        if err != '':
            show_message(err)
            with open(RUNTIME_ERR_FILENAME, 'w') as f:
                f.write(err)
            return

        show_message(out)
        with open(RUNTIME_OUT_FILENAME, 'w') as f:
            f.write(out)
    update()


def setup(plugin):
    """
    Setup function is called by QuickGrader in constructor of the MainWindow.
    Always call functions of dynamic data to ensure that the received data is not stale.

    This plugin system will hopefully be improved. For now, the only capabilities are
    being able to perform operations on the current submission directory.

    This plugin demonstrates the compilation and running of java programs. Stderr and Stdout are
    displayed to the user via a show_message function provided by the ui_delegator contained in the
    Plugin class.

    The ui_delegator just makes sure that the functions called are allowed and then transfers
    control to the QuickGrader class.

    :param plugin: injected plugin class that contains methods for plugin use
    :return: nothing
    """
    plugin.add_action(
        "Run Java",
        lambda filepath: compile_and_run(
            filepath, plugin.get_settings(), plugin.show_message, plugin.ui_delegator.update_fileview
        )
    )
