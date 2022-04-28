from typing import Union
from pathlib import Path


class Paths:
    @staticmethod
    def __research_separation(research_result: list[Path]) -> Union[Path, list[Path], None]:
        """Applies a return types separation based on the research result.

        Args:
            research_result (list[Path]): The default result of the research.

        Returns:
            Union[list[Path], None]: A list of Paths if multiple results and None of nothing found.
        """
        
        res_len = len(research_result)
        
        if res_len < 1:
            return None
        else:
            return research_result
    
    
    @staticmethod
    def search_file_in_top_layer(dir_path: Path, filename: str) -> Union[Path, list[Path], None]:
        """Search a file based on its name only inside the top layer of a directory.

        Args:
            dir_path (Path): The path of the directory where to search.
            filename (str): The name of the file to search.

        Returns:
            Union[list[Path], None]: A list of Paths if multiple results and None of nothing found.
        """
        
        if dir_path.exists() and dir_path.is_dir():
            top_layer = list(dir_path.iterdir())
            result = None
            
            for item in top_layer:    
                if filename == item.name:
                    result = top_layer
                    
            if result is not None:
                return Paths.__research_separation(result)
        
        return None
    
    
    @staticmethod
    def search_file_in_glob(dir_path: Path, filename: str) -> Union[list[Path], None]:
        """Search a file based on its name inside a whole directory (global).

        Args:
            dir_path (Path): The path of the directory where to search.
            filename (str): The name of the file to search.

        Returns:
            Union[list[Path], None]: A list of Paths if multiple results and None of nothing found.
        """
        
        if dir_path.exists() and dir_path.is_dir():
            result = list(dir_path.glob(f"**/{filename}"))
            
            return Paths.__research_separation(result)
        
        return None
