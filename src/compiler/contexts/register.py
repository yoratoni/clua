from typing import Optional, TextIO, MutableSequence
from array import array


class Register:
    """Used as a context/storage for instructions between the scanner and the parser."""
    
    # Currently opened clua file object
    cf_object: Optional[TextIO] = None
      
    # Register virtual pointer (needs to be updated by the real pointer position).
    cf_virtual_pointer_pos: int = 0
    
    # Contains the length of every read line
    # It is used after the first reading of the file
    # if the parser ask for a re-scanning of certain lines
    cf_line_lengths: MutableSequence[int] = array("i")
    
    # -1 removes the first iteration supplement (0-Indexing)
    cf_line_number: int = -1  
    
    # Stores the currently processed line
    cf_line: str = ""
