from compiler import Paths, Cache, Loader
from pathlib import Path

import xxhash


example_dir_path = Path.joinpath(Path.cwd(), "tests", "clua")

Loader.load(example_dir_path)

print(Cache.Compiler.compiler_tree)
print("")
print(Cache.Compiler.loaded_data)
print("")
print(Cache.Project.project_tree)
print("")
print(Cache.Project.loaded_configs)