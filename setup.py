import cx_Freeze
import os
from cx_Freeze import setup, Executable


include_files = ["assets", "assets", "database"]


build_exe_options = {
    "packages": ["os", "customtkinter", "sqlite3", "bcrypt"],
    "include_files": include_files,
}


executables = [
    Executable("app.py", base="Win32GUI", icon="assets/icons/python.ico")
]


setup(
    name="Sistema de Login",
    version="1.0",
    description="Sistema de login",
    options={"build_exe": build_exe_options},
    executables=executables
)