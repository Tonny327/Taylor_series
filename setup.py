from cx_Freeze import setup, Executable

setup(
    name="Taylor_series",
    version="1.0",
    description="Разложение тригонометрических функций в ряд Тейлора",
    executables=[Executable("Taylor_series.py", base="Win32GUI", icon="icon_for_taylor.ico")],
    target_dir = r"D:\BGAS_study\Python\kurss"
)