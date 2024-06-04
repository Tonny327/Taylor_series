import sys
from cx_Freeze import setup, Executable

# Определяем дополнительные зависимости
build_exe_options = {
    "packages": ["os", "sys", "PyQt5", "matplotlib"],
    "excludes": [],
    "include_files": [
        (r"D:\BGAS_study\Python\kurss\icon_for_taylor.ico", "icon_for_taylor.ico")
    ],
    "include_msvcr": True,  # Включает библиотеки MS Visual C++ Runtime
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Taylor_series",
    version="1.0",
    description="Разложение тригонометрических функций в ряд Тейлора",
    options={"build_exe": build_exe_options},
    executables=[Executable("Taylor_series.py", base=base, icon="icon_for_taylor.ico")],
)