from compiler import Operator, Register, Loader, Cache
from pathlib import Path


def main():
    clua_files_dir_path = Path.joinpath(Path.cwd(), "tests", "clua_files")
    # example_file_path = Path.joinpath(clua_files_dir_path, "mul_lines.clua")


    Loader.initialize(clua_files_dir_path)
    print(Cache.Compiler.compiler_database)


    # example_file = Operator.open_cf(example_file_path)
    
    # curr_line = "."
    
    # while not Operator.cf_is_eof(curr_line):
    #     print("****")
    #     curr_line = Operator.cf_readline(example_file)
    #     print(curr_line)
    #     print(f"Line Count: {Register.cf_line_count}")
    #     print(f"Line Lengths: {Register.cf_line_lengths}")
    #     print(f"Register pointer position: {Operator.VirtualPointer.get_position()}")
        

    # Operator.close_cf(example_file)


if __name__ == "__main__":
    main()
    