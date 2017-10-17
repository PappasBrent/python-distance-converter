import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:/Users/Brent/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'C:/Users/Brent/AppData/Local/Programs/Python/Python36/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['C:/Users/Brent/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll',
                   'C:/Users/Brent/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll']
)

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Array of files to convert to executables (only one)
executables=[Executable('DistanceConverter.py', base=base)]

# Details
setup(name='Distance Converter',
      version = '1.0',
      description = 'Basic distance converter',
      options = dict(build_exe = buildOptions),
      executables = executables)
