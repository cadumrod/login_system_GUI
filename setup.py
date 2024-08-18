import sys
import os
from cx_Freeze import setup, Executable


files = [
    ('assets/icons/', 'assets/icons/'),
    ('database/', 'database/')
]


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


executables = [
    Executable(
        script='app.py',
        base=base,
        icon='assets/icons/python.ico'
    )
]


setup(
    name='Sistema de login',
    version='1.0',
    description='Sistema de login desenvolvido em python e SQLite3',
    author='Carlos Rodrigues',
    options={
        'build_exe': {
            'packages': ['os', 'customtkinter', 'sqlite3', 'bcrypt'],
            'include_files': files,
        }
    },
    executables=executables
)
