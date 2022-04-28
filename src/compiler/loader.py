from copy import deepcopy
from typing import Union
from pathlib import Path

from compiler import Paths

import yaml


class Loader:
    @staticmethod
    def load_yaml(yaml_path: Path) -> Union[dict, None]:
        """Loads a YAML file based on its path,
        acts as a universal YAML file loader wrapper.

        Note:
            Empty files are included but with an empty dict.

        Args:
            yaml_path (Path): The path of the YAML file to load.

        Returns:
            Union[dict, None]: Content of the YAML file formatted as a string,
                or None if file not found/yaml error.
        """
        
        if yaml_path is not None and yaml_path.exists():
            with open(yaml_path, "r") as yaml_file:
                try:
                    content = yaml.load(yaml_file, yaml.FullLoader)
                    
                    if isinstance(content, dict):
                        return content
                    
                    # Include empty files
                    if content is None:
                        return {}
                
                # Ensure default loading
                except yaml.YAMLError:
                    return None
                
        return None

    
    @staticmethod
    def load_config(project_path: Path, filename: str = "clua.config.yaml") -> Union[dict, None]:
        """Loads one or multiple user project config files and returns them into a dict
        where the keys are the project directory names where the file is located (localized configs).

        Note:
            - Multiple localized config files.
            - Applies default values if the all the config files are unavailable.

        Args:
            project_path (Path): The project CWD Path where to search the config file.
            filename (str, optional): The config filename ("clua.config.yaml")

        Returns:
            Union[dict, None]: The loaded config file dict.
        """
        
        # User project config file
        result = Paths.search_file_in_glob(project_path, filename)

        # Default config replacement
        if result is None:
            result = [Path.cwd().joinpath("src", "data", filename)]

        res_dict = {}
        
        for path in result:
            config_content = Loader.load_yaml(path)
            
            if config_content is not None:
                res_dict[path.parent] = deepcopy(config_content)
                
        return res_dict
