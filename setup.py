from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files=[
    'assets',
    'themes',
    'plugins'
])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('main.py', base=base)
]

setup(name='QuickGrader',
      version = '1.0',
      description = 'An extensible grade program that allows users to grade student submissions from Canvas.',
      options = dict(build_exe = buildOptions),
      executables = executables)
