from typing import Union
from pathlib import Path


class Paths:
    @staticmethod
    def __research_separation(research_result: Union[list[Path], None]) -> Union[Path, list[Path], None]:
        """Applies a return types separation based on the research result.

        Args:
            research_result (Union[list[Path], None]): The default result of the research.

        Returns:
            Union[list[Path], None]: A list of Paths if multiple results and None of nothing found.
        """
        
        if research_result is None:
            return None
        
        if isinstance(research_result, list):
            if len(research_result) < 1:
                return None
            else:
                return research_result
            
        return None
    
    
    @staticmethod
    def search_by_filename(dir_path: Path, filename: str, is_recursive: bool) -> Union[list[Path], None]:
        """Allows to search a file by its filename, supports multiple instances of the file
        which means that the returned result is a list of Paths even with one result
        or None if nothing found.
        
        Notes about "is_recursive":
        - False: search only inside the top layer of a directory.
        - True: search inside a whole directory include child directories, etc..

        Args:
            dir_path (Path): The path of the directory where to search.
            filename (str): The name of the file to search.

        Returns:
            Union[list[Path], None]: A list of Paths if one or multiple results
                and None of nothing found.
        """
        
        if dir_path.exists() and dir_path.is_dir():
            if not is_recursive:
                top_layer = list(dir_path.iterdir())
                result = None
                
                for item in top_layer:    
                    if filename == item.name:
                        result = top_layer
            else:
                result = list(dir_path.glob(f"**/{filename}"))
                
            return Paths.__research_separation(result)
        
        return None
