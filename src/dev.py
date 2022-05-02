from compiler import Paths, Cache, Loader
from pathlib import Path

import xxhash


example_dir_path = Path.joinpath(Path.cwd(), "tests", "clua")

Loader.loader()

print(Cache.Compiler.data["diagnostic_messages"])