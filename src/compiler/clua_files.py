from compiler import Paths, Register

from typing import Optional, TextIO
from pathlib import Path


class CluaFiles:
    """Note: the default 'clua_file_' name is abbreviated as 'cf_'."""
    
    
    class Pointer:
        """Operations on a already opened Clua file pointer."""
        
        @staticmethod
        def get_register_pointer_pos() -> int:
            """Returns the pointer position from the Register."""

            return Register.cf_pointer_pos
        
        
        @staticmethod
        def set_register_pointer_pos(new_pointer_pos: int):
            """Set the Register pointer position value."""
        
            Register.cf_pointer_pos = new_pointer_pos
        
        
        @staticmethod
        def get_then_set_register_pointer_pos(new_pointer_pos: int) -> int:
            """Get the old pointer position from the register before setting a new one."""
        
            old_pointer_pos = CluaFiles.Pointer.get_pointer_pos()
            CluaFiles.Pointer.set_pointer_pos(new_pointer_pos)
            return old_pointer_pos
        
        
        @staticmethod
        def get_pointer_pos_difference_from_register(new_pointer_pos: int) -> int:
            """
            Returns the difference between the Register and the current pointer positions.

            Args:
                new_pointer_pos (int): The new pointer position.

            Returns:
                int: The difference between the two pointer positions.
            """
            
            return new_pointer_pos - CluaFiles.Pointer.get_register_pointer_pos()


    @staticmethod
    def open_cf(cf_path: Path) -> Optional[TextIO]:
        """
        Opens a .clua file for future reading, note that this method don't close the file
        as it should be kept inside the memory for parser later re-scanning.
        
        Args:
            cf_path (Path): The path of the file that will be scanned.
            
        Returns:
            Optional[TextIO]: Successfully loaded file object or None if the file cannot be opened.
        """
    
        if Paths.is_file_path_valid(cf_path, ".clua"):
            try:
                return open(cf_path, "r")
            except OSError:
                pass
        
        return None
    
    
    @staticmethod
    def close_cf(cf_object: TextIO) -> bool:
        """
        Closes a previously opened .clua file (Parser final validity instruction or eq.).
        
        Args:
            cf_object (TextIO): The file object (TextIO -> open() returned object).
        """
        
        if isinstance(cf_object, TextIO):
            cf_object.close()
            return True
        
        return False


    @staticmethod
    def cf_readline(cf_object: TextIO) -> str:
        
        current_line = cf_object.readline()
        
        CluaFiles.Pointer.set_register_pointer_o(cf_object)
        Register.cf_line_count += 1
        Register.cf_line_lengths.append(len(current_line))
        