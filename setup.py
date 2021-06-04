import sys
import os
from cx_Freeze import setup,Executable

files = []

target = Executable(
    script='window.py',
    base='win32GUI',
    icon='win_pic.png'
)

setup(
    name='Template',
    version='1.0',
    outhor='Wajdi Alsalti',
    options={'build_exe':{'include_files':files}},
    executables=[target]
)