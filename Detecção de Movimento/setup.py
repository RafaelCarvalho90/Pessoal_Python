import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Para criar um executável GUI no Windows

executables = [Executable("base.py", base=base)]

setup(
    name="GatoFDP",
    version="1.0",
    description="Descrição do executável",
    executables=executables,
)
