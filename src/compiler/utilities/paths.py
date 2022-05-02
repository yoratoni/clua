from typing import Generator, Union
from pathlib import Path


class Paths:
    @staticmethod
    def is_file_path_valid(file_path: Path, extension: str = None) -> bool:
        """Returns True if a path led to a valid file.
        """
        
        if file_path is not None and file_path.exists() and file_path.is_file():
            if (extension is None) or (extension is not None and file_path.suffix() == extension):
                return True
        
        return False
    
    
    @staticmethod
    def is_dir_path_valid(dir_path: Path) -> bool:
        """Returns True if a path led to a valid directory.
        """
        
        if dir_path is not None and dir_path.exists() and dir_path.is_dir():
            return True
        
        return False
    

    @staticmethod
    def get_directory_tree(dir_path: Path, include_child_dirs: bool) -> Generator[Path, None, None]:
        """Returns a directory tree depending on the recursive parameter (glob or iterdir).

        Args:
            dir_path (Path): The path of the directory to generate the tree of.
            include_child_dirs (bool): Recursive research inside the dir (multiple layers).

        Returns:
            Generator[Path]: A generator object that contains the list of dir paths.
        """
        
        if not include_child_dirs:
            dir_tree = dir_path.iterdir()
        else:
            # Universal pattern including all files
            dir_tree = dir_path.glob("**/*")
            
        return dir_tree
    

    @staticmethod
    def search_path_in_tree_by_name(tree: list[Path], name: str) -> Union[Path, None]:
        """Search for a path where the last component have a certain name.
        Acts as a simple research, only the first valid path is returned.
        
        Args:
            tree (list[Path]): The tree where to search.
            name (str): The name to search, note that this field is case-sensitive.
            
        Returns: 
            Union[Path, None]: The path where the last component is the name.
        """
        
        if tree is not None:
            for path in tree:
                if path.name == name:
                    return path
            
        return None

    
    @staticmethod
    def search_by_extensions(dir_path: Path, extensions: set[str], include_child_dirs: bool) -> Union[list[Path], None]:
        """Returns the path of all the files that matches one of the listed extensions.
        
        Args:
            dir_path (Path): The path of the directory where to search.
            extensions (set[str]): A filter of extensions (included).
            include_child_dirs (bool): Recursive research inside the dir (multiple layers).

        Returns:
            Union[list[Path], None]: Paths that matches the extensions filter,
                or None if the path is invalid.
        """
        
        if Paths.is_dir_path_valid(dir_path):
            dir_list = Paths.get_directory_tree(dir_path, include_child_dirs)

            # Generate matching suffixes list
            result = list(path.resolve() for path in dir_list if path.suffix in extensions)
            
            return result
            
        return None
    
    
    @staticmethod
    def search_by_name(dir_path: Path, name: str, include_child_dirs: bool) -> Union[list[Path], None]:
        """Returns the path of all the files/directories that have this name.

        Args:
            dir_path (Path): The path of the directory where to search.
            name (str): The name of the file/directory to search the path of.
            include_child_dirs (bool): Recursive research inside the dir (multiple layers).

        Returns:
            Union[list[Path], None]: Path of the files that matches the filename,
                or None if the path is invalid.
        """
        
        if Paths.is_dir_path_valid(dir_path):
            dir_list = Paths.get_directory_tree(dir_path, include_child_dirs)

            # Generate matching filenames list
            result = list(path.resolve() for path in dir_list if path.name == name)
            
            return result
            
        return None
