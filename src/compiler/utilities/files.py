from compiler import Paths

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
            Union[dict, None]: Content of the YAML file formatted as a string,
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
                
                # DPC102
                except yaml.YAMLError:
                    return None
                
        return None


    @staticmethod
    def load_yaml_from_tree(
        tree: list[Path],
        filename: str,
        include_empty_file: bool = False
    ) -> Union[dict, None]:
        """Loads a YAML file from a tree (paths list).

        Args:
            tree (list[Path]): The tree where to search the file path.
            filename (str): The name of the file to found.
            include_empty_file (bool, optional): Empty file returned as an empty dict if True.

        Returns:
            Union[dict, None]: Content of the YAML file formatted as a string,
                or None if file not found/yaml error.
        """

        if tree is not None:
            res_path = Paths.search_path_in_tree_by_name(tree, filename)
            
            return Files.load_yaml(res_path, include_empty_file)
            
        return None
