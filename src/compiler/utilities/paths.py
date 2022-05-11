from typing import Generator, Optional
from pathlib import Path


class Paths:
    @staticmethod
    def is_file_path_valid(file_path: Path, extension: str = None) -> bool:
        """(General method) Return True if a file path is valid + optional extension validity."""
        
        if file_path is None:
            return False
        
        if not file_path.exists():
            return False
        
        if not file_path.is_file():
            return False
        
        if extension is not None and file_path.suffix != extension:
            return False
  
        return True


    @staticmethod
    def is_dir_path_valid(dir_path: Path) -> bool:
        """(General method) Return True if a dir path is valid."""
        
        if dir_path is None:
            return False
        
        if not dir_path.exists():
            return False
        
        if not dir_path.is_dir():
            return False
        
        return True


    @staticmethod
    def get_directory_tree(dir_path: Path, include_child_dirs: bool) -> Generator[Path, None, None]:
        """
        Returns a directory tree depending on the recursive parameter (glob or iterdir).

        Args:
            dir_path (Path): The path of the directory to generate the tree of.
            include_child_dirs (bool): Recursive research inside the directory (multiple layers).

        Returns:
            Generator[Path, None, None]: A generator that contains the list of directory paths.
        """
        
        if not include_child_dirs:
            return dir_path.iterdir()

        # Universal pattern including all files
        return dir_path.glob("**/*")


    @staticmethod
    def search_paths_in_tree_by_name(tree: list[Path], name: str) -> Optional[list[Path]]:
        """
        Search for one or multiple paths where the last component have a certain name.
        
        Args:
            tree (list[Path]): The tree where to search.
            name (str): The name to search, note that this field is case-sensitive.
            
        Returns: 
            Optional[list[Path]]: Paths where the last component is equal to the name parameter
                or None if the tree is invalid.
        """
        
        if tree is not None:
            paths: list[Path] = []
            
            for path in tree:
                if path.name == name:
                    paths.append(path)

            return paths
        
        return None


    @staticmethod
    def search_paths_in_tree_by_extension(tree: list[Path], extension: str) -> Optional[list[Path]]:
        """
        Search for one or multiple paths where the last component is a file with a certain extension.
        
        Args:
            tree (list[Path]): The tree where to search.
            extension (str): The extension/suffix of the files to include.
            
        Returns: 
            Optional[list[Path]]: Paths where the last component is a file with a suffix equal
                to the extension parameter or None if the tree is invalid.
        """
        
        if tree is not None:
            paths: list[Path] = []
            
            for path in tree:
                if Paths.is_file_path_valid(path, extension):
                    paths.append(path)

            return paths
        
        return None

    
    @staticmethod
    def search_by_extensions(
        dir_path: Path,
        extensions: set[str],
        include_child_dirs: bool
    ) -> Optional[list[Path]]:
        """
        Returns the path of all the files that matches one of the listed extensions.
        
        Args:
            dir_path (Path): The path of the directory where to search.
            extensions (set[str]): A filter of extensions (included).
            include_child_dirs (bool): Recursive research inside the directory (multiple layers).

        Returns:
            Optional[list[Path]]: Paths that matches the extensions filter,
                or None if the path is invalid.
        """
        
        if Paths.is_dir_path_valid(dir_path):
            dir_list: Generator[Path, None, None] = Paths.get_directory_tree(
                dir_path,
                include_child_dirs
            )

            # Generate matching suffixes list
            result: list[Path] = list(
                path.resolve() for path in dir_list
                if path.suffix in extensions
            )
            
            return result
            
        return None


    @staticmethod
    def search_by_name(dir_path: Path, name: str, include_child_dirs: bool) -> Optional[list[Path]]:
        """
        Returns the path of all the files/directories that have this name.

        Args:
            dir_path (Path): The path of the directory where to search.
            name (str): The name of the file/directory to search the path of.
            include_child_dirs (bool): Recursive research inside the directory (multiple layers).

        Returns:
            Optional[list[Path]]: Path of the files that matches the filename,
                or None if the path is invalid.
        """
        
        if Paths.is_dir_path_valid(dir_path):
            dir_list: Generator[Path, None, None] = Paths.get_directory_tree(
                dir_path,
                include_child_dirs
            )

            # Generate matching filenames list
            result: list[Path] = list(
                path.resolve() for path in dir_list
                if path.name == name
            )
            
            return result
            
        return None
    
    
    @staticmethod
    def clua_paths_organizer(project_tree: list[Path]) -> Optional[list[Path]]:
        """
        Get the path of all the valid clua files and sorts them by directory depth.

        Args:
            project_tree (list[Path]): The loaded user project tree.

        Returns:
            Optional[list[Path]]: A directory depth sorted list of clua file paths.
        """
        
        unsorted_paths: Optional[list[Path]] = Paths.search_paths_in_tree_by_extension(
            project_tree,
            ".clua"
        )
        
        # General output verification
        if isinstance(unsorted_paths, list) and len(unsorted_paths) > 0:
            # Reversed Stem sorting (directory depth optimization)
            return sorted(unsorted_paths, key=lambda i: i.stem, reverse=True)
        
        return None
