from compiler import Loader
from pathlib import Path

CWD = Path.cwd()

print(Loader.load_config(CWD))
