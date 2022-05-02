from regex import F
from compiler import Paths, Files, Cache

from copy import deepcopy
from typing import Union
from pathlib import Path

import sys


class Loader:
    @staticmethod
    def load_compiler_tree(
        data_dir_path: Path,
        included_extensions: list[str] = [".yaml"]
    ) -> Union[list[Path], None]:
        """Loads the compiler tree with whitelisted file extensions,
        saves it into the Compiler sub-class cache and returns the list of found paths.

        Args:
            data_dir_path (Path): Path to the data directory.
            included_extensions (list[str], optional): File extensions included into the tree.

        Returns:
            list[Path]: The result list of paths after the scanning of the compiler dir.
        """

        # Data directory research
        compiler_tree = Paths.search_by_extensions(data_dir_path, included_extensions, True)
        
        # Empty list catching
        if len(compiler_tree) > 0:
            return compiler_tree
        
        return None


    @staticmethod
    def load_diagnostic_messages(
        compiler_tree: list[Path],
        filename: str = "diagnostic_messages.yaml"
    ) -> Union[dict, None]:
        """_summary_

        Args:
            filename (str): _description_

        Returns:
            Union[dict, None]: _description_
        """
        
        diagnostic_messages = Files.load_yaml_from_tree(compiler_tree, filename, False)
        
        if diagnostic_messages is not None:
            return diagnostic_messages
        
        return None
        
                    
    @staticmethod
    def load_project_tree(project_path: Path) -> Union[list[Path], None]:
        """_summary_
        """


    @staticmethod
    def load_config_files() -> Union[list[Path], None]:
        """_summary_
        """


    @staticmethod
    def loader():
        """Project/Compiler loading global wrapper.
        
        Ordering:
            - Load Compiler Tree.
            - Load Diagnostic Messages.
            - Load Project Tree.
            - Load Config Files.
            
        Returns:
            Cache.Compiler/Cache.Project: Global cached variables.
        """
        
        # DPC103 DPC104
        data_path = Path(__file__).parent

        if Paths.is_dir_path_valid(data_path):
            compiler_tree = Loader.load_compiler_tree(data_path)
            
            if compiler_tree is not None:
                diagnostic_messages = Loader.load_diagnostic_messages(compiler_tree)
                
                if diagnostic_messages is not None:
                    Cache.Compiler.data["diagnostic_messages"] = diagnostic_messages
