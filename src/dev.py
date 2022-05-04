from compiler import Paths, Cache, Loader
from pathlib import Path


def main():
    example_dir_path = Path.joinpath(Path.cwd(), "tests", "clua")

    Loader.load(example_dir_path)
    print(Cache.Project.clua_files)


if __name__ == "__main__":
    main()
    