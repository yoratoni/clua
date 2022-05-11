from compiler import Paths, Files, Cache

from typing import Generator, Optional
from pathlib import Path


class Loader:
    @staticmethod
    def load_compiler_tree(
        data_dir_path: Path,
        included_extensions: list[str] = None
    ) -> Optional[list[Path]]:
        """
        Loads the compiler tree with whitelisted file extensions.

        Args:
            data_dir_path (Path): Path to the data directory.
            included_extensions (List[str], optional): File extensions included into the tree.
                Defaults to a list -> [".yaml"].

        Returns:
            Optional[list[Path]]: The result list of paths after the scanning
                of the compiler directory.
        """
        
        # Default arg value can't be a mutable object
        if included_extensions is None:
            included_extensions = [".yaml"]

        # Data directory research
        compiler_tree: Optional[list[Path]] = Paths.search_by_extensions(
            data_dir_path,
            included_extensions,
            True
        )
        
        # Empty list catching
        return compiler_tree if len(compiler_tree) > 0 else None


    @staticmethod
    def load_compiler_data(
        compiler_tree: list[Path],
        data_filenames: list[str]
    ) -> dict[Optional[dict]]:
        """
        Loads the YAML files that contains the diagnostic messages used by the debugger
        and the default config file of the compiler from the loaded compiler tree.

        Args:
            compiler_tree (list[Path]): The loaded compiler tree.
            data_filenames (list[str]): The name of the files to load into loaded_data.
            
        Returns:
            dict[Optional[dict]]: Inside the main dict, the keys are the filenames,
                and the values are the files content formatted as dicts,
                or None if file not found/YAML error.
        """
        
        loaded_data = {}
        
        for filename in data_filenames:
            content: Optional[dict] = Files.load_yaml_from_compiler_tree(compiler_tree, filename)
            
            if content is not None:
                loaded_data[filename] = content
        
        # Default empty return
        return loaded_data


    @staticmethod
    def load_project_tree(project_dir_path: Path) -> Optional[list[Path]]:
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
            
            if isinstance(project_tree_generator, Generator):
                project_tree = list(project_tree_generator)
                
                # Empty list catching
                if len(project_tree) > 0:
                    return project_tree
                 
        return None


    @staticmethod
    def load_project_configs(
        project_tree: list[Path],
        filename: str = "clua.config.yaml"
    ) -> Optional[dict[dict]]:
        """
        Loads all the found config files inside the user project.
        
        Args:
            project_tree (list[Path]): The loaded user project tree.
            filename (str, optional): The default name of the clua config file.
            
        Returns:
            Optional[dict[dict]]: Contains all the loaded config files,
                the keys corresponds to the path of these files,
                the values are their dict formatted content.
        """

        # DPC102
        # Load the content of all the found config files
        return Files.load_multiple_yaml_from_tree(project_tree, filename)


    @staticmethod
    def load(project_dir_path: Path) -> bool:
        """
        Loads the compiler tree/data and the project tree/configs,
        acts as the main Loader wrapper.

        Args:
            project_dir_path (Path): The path to the project directory.

        Returns:
            bool: True if everyting is correctly loaded.
        """
        
        # Loading results
        compiler_loading_res = False
        project_loading_res = False
        
        # Compiler data relative path
        data_path = Path(__file__).parent
        
        # Compiler loading part
        if Paths.is_dir_path_valid(data_path):
            compiler_tree = Loader.load_compiler_tree(data_path)
            
            if compiler_tree is not None:
                # List of filenames used to load the compiler data (src/compiler/data)
                data_filenames = ["diagnostic_messages.yaml", "clua.config.yaml"]
                
                Cache.Compiler.compiler_tree = compiler_tree
                Cache.Compiler.loaded_data = Loader.load_compiler_data(compiler_tree, data_filenames)
                compiler_loading_res = True
                
        # Project loading part
        if Paths.is_dir_path_valid(project_dir_path):
            project_tree = Loader.load_project_tree(project_dir_path)
            
            if project_tree is not None:
                Cache.Project.project_tree = project_tree
                Cache.Project.clua_files = Paths.clua_paths_organizer(project_tree)
                Cache.Project.loaded_configs = Loader.load_project_configs(project_tree)
                project_loading_res = True
        
        # Two loading part bool res
        return compiler_loading_res and project_loading_res
    