from compiler import Loader
from pathlib import Path

compiler_path = Path.cwd().joinpath("src")
test_project_path = Path.joinpath(Path.cwd().joinpath("tests", "clua"))

print(Loader.load_diagnostics())
