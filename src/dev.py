from compiler import Paths, Cache, Loader, CluaFiles
from pathlib import Path


def main():
    example_dir_path = Path.joinpath(Path.cwd(), "tests", "clua")
    example_file_path = Path.joinpath(example_dir_path, "dev.clua")


    example_file = CluaFiles.open_cf(example_file_path)
    
    for i in range(5):
        print(example_file.readline().strip())
        print(f"Register pointer position: {CluaFiles.Pointer.get_register_pointer_pos()}")
        print("****")

    CluaFiles.close_cf(example_file)


if __name__ == "__main__":
    main()
    