import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","tkinter","webbrowser","csv","PIL","queue",'geopy',"random","time","threading","MiniScripts","AppGUI","search_algorithm","requests"],'include_files':["assets"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "ShowMeTheWay",
    version = "1.1",
    description = "Simple pathfinding GUI app",
    options = {"build_exe": build_exe_options},
    executables = [Executable("ShowMeTheWay.py", base=base)]
)