from compiler import Paths, Files, Cache

from typing import Dict, Any, Generator, Optional
from pathlib import Path

import sys


class Loader:
    @staticmethod
    def __load_compiler_tree(
        compiler_dir_path: Path,
        included_extensions: Optional[list[str]] = None
    ) -> Optional[list[Path]]:
        """
        Loads the compiler tree with whitelisted file extensions.

        Args:
            compiler_dir_path (Path): The path of the main compiler directory.
            included_extensions (List[str], optional): File extensions included into the tree.
                Defaults to a list -> [".yaml"].

        Returns:
            Optional[list[Path]]: The result list of paths after the scanning
                of the compiler directory.
        """
        
        # Default arg value can't be a mutable object
        # Replaced by YAML extension (database main files)
        if included_extensions is None:
            included_extensions = [".yaml"]

        # Data directory research
        compiler_tree: Optional[list[Path]] = Paths.search_by_extensions(
            compiler_dir_path,
            included_extensions,
            True
        )
        
        # Empty list catching
        if compiler_tree is not None:
            return compiler_tree if len(compiler_tree) > 0 else None


    @staticmethod
    def __load_compiler_data(
        compiler_tree: list[Path],
        data_filenames: list[str]
    ) -> Dict[str, Optional[Dict[str, Any]]]:
        """
        Loads the YAML files that contains the diagnostic messages used by the debugger
        and the default config file of the compiler from the loaded compiler tree.

        Args:
            compiler_tree (list[Path]): The loaded compiler tree.
            data_filenames (list[str]): The name of the files to load into loaded_data.
            
        Returns:
            Dict[str, Optional[Dict[str, Any]]]: The keys are the filenames,
                and the values are the files content formatted as dicts,
                or None if file not found/YAML error.
        """
        
        loaded_data: Dict[str, Optional[Dict[str, Any]]] = {}
        
        for filename in data_filenames:
            content: Optional[Dict[str, Any]] = Files.load_yaml_from_compiler_tree(
                compiler_tree,
                filename
            )
            
            if content is not None:
                loaded_data[filename] = content
        
        # Default empty return
        return loaded_data


    @staticmethod
    def __load_project_tree(project_dir_path: Path) -> Optional[list[Path]]:
        """
        Returns a tree that contains all the files and directories
        inside a project, including the child directories.

        Args:
            project_dir_path (Path): The path of the project directory.

        Returns:
            Optional[list[Path]]: A list of all the paths found inside the project dir
                or None if the path is invalid.
        """

        if Paths.is_dir_path_valid(project_dir_path):
            project_tree_generator: Generator[Path, None, None] = Paths.get_directory_tree(
                project_dir_path,
                True
            )
            
            project_tree = list(project_tree_generator)
            
            # Empty list catching
            if len(project_tree) > 0:
                return project_tree
                 
        return None


    @staticmethod
    def __load_project_configs(
        project_tree: list[Path],
        filename: str = "clua.config.yaml"
    ) -> Optional[Dict[Path, Any]]:
        """
        Loads all the found config files inside the user project.
        
        Args:
            project_tree (list[Path]): The loaded user project tree.
            filename (str, optional): The default name of the clua config file.
            
        Returns:
            Optional[Dict[Path, Any]]: Contains all the loaded config files,
                the keys corresponds to the path of these files,
                the values are their dict formatted content.
        """

        # DPC102
        # Load the content of all the found config files
        return Files.load_multiple_yaml_from_tree(project_tree, filename)


    @staticmethod
    def __load_compiler(compiler_dir_path: Path) -> bool:
        """Loads the compiler data and saves them to the Cache.

        Args:
            compiler_dir_path (Path): The path of the main compiler directory.

        Returns:
            bool: True if all the data are successfully loaded.
        """
        
        if Paths.is_dir_path_valid(compiler_dir_path):
            # Loads a general tree containing all the paths found inside the compiler directory
            compiler_tree: Optional[list[Path]] = Loader.__load_compiler_tree(compiler_dir_path)
            
            if compiler_tree is not None:
                # List of filenames used to load the compiler data (compiler/data)
                data_filenames = [
                    "diagnostic_messages.yaml",
                    "clua.config.yaml",
                    "tokens.yaml"
                ]
                
                Cache.Compiler.compiler_tree = compiler_tree
                Cache.Compiler.compiler_database = Loader.__load_compiler_data(
                    compiler_tree,
                    data_filenames
                )
                
                return True
            
        return False


    @staticmethod
    def __load_project(project_dir_path: Path) -> bool:
        """Loads the project directory data and saves them into the Cache (project sub-class).

        Args:
            project_dir_path (Path): The path of the project directory.

        Returns:
            bool: True if all the data are successfully loaded.
        """

        if Paths.is_dir_path_valid(project_dir_path):
            project_tree: Optional[list[Path]] = Loader.__load_project_tree(project_dir_path)
            
            if project_tree is not None:
                Cache.Project.project_tree = project_tree
                Cache.Project.clua_trace = Paths.clua_paths_organizer(project_tree)
                Cache.Project.loaded_config_dicts = Loader.__load_project_configs(project_tree)
                
                return True
        
        return False


    @staticmethod
    def initialize(project_dir_path: Path):
        """
        Initialize the compiler tree/data and the project tree/configs,
        acts as the main Loader method..

        Args:
            project_dir_path (Path): The path of the project directory.
        """
        
        # DPC103
        compiler_dir_path = Path(__file__).parent
        
        compiler_loading_result = Loader.__load_compiler(compiler_dir_path)
        project_loading_result = Loader.__load_project(project_dir_path)
                
        if not compiler_loading_result or not project_loading_result:
            sys.exit(1)

    