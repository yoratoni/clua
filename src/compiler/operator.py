from compiler import Paths, Register

from typing import Optional, TextIO
from pathlib import Path


class Operator:
    """
    A utility class used for the operations on Clua files.
    
    Note:
        The default 'clua_file_' name is abbreviated as 'cf_'.
    """
    
    class VirtualPointer:
        """Operations on a already opened Clua file pointer."""
        
        @staticmethod
        def get_position() -> int:
            """Returns the virtual pointer position from the Register."""

            return Register.cf_virtual_pointer_pos
        
        
        @staticmethod
        def set_position(new_pointer_pos: int):
            """Set the Register virtual pointer position."""
        
            Register.cf_virtual_pointer_pos = new_pointer_pos
        
        
        @staticmethod
        def update_position(new_pointer_pos: int) -> int:
            """Get the virtual pointer position from the Register before setting a new one."""
        
            old_virtual_pointer_pos = Operator.VirtualPointer.get_position()
            Operator.VirtualPointer.set_position(new_pointer_pos)
            return old_virtual_pointer_pos
        
        
        @staticmethod
        def get_position_difference(new_pointer_pos: int) -> int:
            """
            Returns the difference between the Register virtual pointer position and the current one.

            Args:
                new_pointer_pos (int): The new pointer position.

            Returns:
                int: The difference between the two pointer positions.
            """
            
            return new_pointer_pos - Operator.VirtualPointer.get_position()


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
    def close_cf(cf_object: Optional[TextIO]) -> bool:
        """
        Closes a previously opened .clua file (Parser final validity instruction or eq.).
        
        Args:
            cf_object (Optional[TextIO]): The file object (TextIO -> open() returned object).
        """
        
        if isinstance(cf_object, TextIO):
            cf_object.close()
            return True
        
        return False


    @staticmethod
    def cf_is_eof(current_line: str) -> bool:
        """Returns True if the end of the file (EOF) is reached."""
        
        if not current_line:
            return True
        
        return False


    @staticmethod
    def cf_readline(cf_object: TextIO) -> str:
        """
        Reads a line from the Clua file object based on the current pointer position
        and updates the corresponding Register values.

        Args:
            cf_object (TextIO): The file object (TextIO -> open() returned object).

        Returns:
            str: The line that have been read.
        """
        
        # DPC105
        current_line = cf_object.readline()

        # Overwrites the virtual pointer pos by the real pointer one
        Operator.VirtualPointer.set_position(cf_object.tell())
        
        # Updates cf line data
        Register.cf_line_lengths.append(len(current_line))
        Register.cf_line_count += 1
        
        return current_line
    