import sys
import os
from cx_Freeze import setup, Executable

files = [('assets/icons/', 'assets/icons/'),
         ('database/', 'database/'),
         'app.py']

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

config = Executable(
    script='app.py',
    icon='assets/icons/python.ico',
    base=base
)

setup(
    name='Sistema de Login',
    version='1.0',
    description='Aplicação de sistema de login',
    author='Carlos Rodrigues',
    options={'build_exe': {'include_files': files}},
    executables=[config]
)
