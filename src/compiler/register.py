from typing import Optional, TextIO


class Register:
    """Ensure communication between the scanner and the parser (Secondary cache system)."""
    
    # Currently opened clua file object
    cf_object: Optional[TextIO] = None
    
    # Clua file handling data
    cf_line: str = ""
    cf_pointer_pos: int = 0
    cf_line_count: int = 0
    cf_line_lengths: list[int] = []
