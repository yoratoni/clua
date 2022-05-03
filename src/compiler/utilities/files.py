from compiler.utilities import Paths

from copy import deepcopy
from pathlib import Path
from typing import Union

import yaml


class Files:
    @staticmethod
    def load_yaml(file_path: Path, include_empty_file: bool = True) -> Union[dict, None]:
        """Based on its path, loads a YAML file content into a dict.
        
        Args:
            file_path (Path): The path of the YAML file to load.
            include_empty_file (bool, optional): Returns an empty dict if the file is empty,
                note that if set to False, empty files content will be returned as None.

        Returns:
            Union[dict, None]: Content of the YAML file formatted as a dict,
                or None if file not found/yaml error.
        """
        
        if Paths.is_file_path_valid(file_path, ".yaml"):
            with open(file_path, "r") as yaml_file:
                try:
                    content = yaml.load(yaml_file, yaml.FullLoader)
                    
                    if isinstance(content, dict):
                        return content
                    
                    # Includes empty files
                    if include_empty_file and content is None:
                        return {}
                
                # The invalidity of the file is confirmed by the returned None.
                except yaml.YAMLError:
                    return None
                
        return None


    @staticmethod
    def load_yaml_from_tree(
        tree: list[Path],
        filename: str
    ) -> Union[dict[dict], None]:
        """Loads one or multiple YAML files from a tree,
        allows to load all the files that have the same name.

        Args:
            tree (list[Path]): The tree where to search for the YAML files.
            filename (str): The name of the file(s) to load.

        Returns:
            Union[dict[dict], None]: The main dict keys are the paths,
                the values are the dict formatted content of the file(s).
        """
        
        file_paths = Paths.search_paths_in_tree_by_name(tree, filename)
        contents = {}

        if isinstance(file_paths, list) and len(file_paths) > 0:
            for path in file_paths:
                contents[path] = Files.load_yaml(path, True)

            # Secured dict by deep copy
            return deepcopy(contents)

        return None
    

    @staticmethod
    def load_yaml_from_compiler_tree(
        compiler_tree: list[Path],
        filename: str,
        default_index: int = -1
    ) -> Union[dict, None]:
        """Loads a unique YAML file from the compiler tree based on its filename.

        Args:
            compiler_tree (list[Path]): The compiler tree.
            filename (str): The name of the file to load.
            default_index (int, optional): If multiple files found, the default index to use,
                note that -1 will always take the last file found.

        Returns:
            Union[dict, None]: The content of the file formatted as a dict
                or None if file not found/YAML error.
        """
        
        compiler_file_paths = Paths.search_paths_in_tree_by_name(compiler_tree, filename)
        
        if isinstance(compiler_file_paths, list) and len(compiler_file_paths) > 0:
            content = Files.load_yaml(compiler_file_paths[default_index], True)

            # Secured dict by deep copy
            return deepcopy(content)
        
        return None
