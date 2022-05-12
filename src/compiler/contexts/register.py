from typing import Optional, TextIO, MutableSequence
from array import array


class Register:
    """Used as a storage for instructions between the scanner and the parser."""
    
    # Currently opened clua file object
    cf_object: Optional[TextIO] = None
      
    # Register virtual pointer (needs to be updated by the real pointer position).
    cf_virtual_pointer_pos: int = 0
    
    # Contains the length of every read line (cf_readline())
    cf_line_lengths: MutableSequence[int] = array("i")
    
    # -1 removes the first iteration supplement (0-Indexing)
    cf_line_count: int = -1  
    
    # Stores the currently processed line
    cf_line: str = ""
