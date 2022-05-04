from compiler import Protocol

from pathlib import Path


class Scanner:
    @staticmethod
    def file_open():
        pass
    
    
    @staticmethod
    def file_close():
        # Change the current file id and the corresponding file path
        pass
    
    
    @staticmethod
    def file_readline() -> str:
        pass
    
    
    @staticmethod
    def trivia_separation(line_number: int) -> list[str]:
        pass
    
    
    @staticmethod
    def terms_to_tokens() -> list[Protocol.Tokens]:
        pass
    