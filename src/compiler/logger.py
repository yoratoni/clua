from pyostra import pyprint


class Logger:
    class LogTypes:
        """Contains default log types used for diagnostics.
        """
        
        # General log types
        CRITICAL = "Critical"
        ERROR = "Error"
        WARN = "Warning"
        MESSAGE = "Message"
        SUGGESTION = "Suggestion"
        
        # Internal compiler log types (C_ prefix)
        C_PREFIX = "CLUA_COMPILER_INTERNAL_LOG"
        C_FILE_NOT_FOUND = "FileNotFound"
        
    
    @staticmethod
    def custom_log(log_type: str, msg: str, is_internal: bool):
        """Allows to print a custom log outside of default diagnostic codes.

        Args:
            log_type (str): The type of the log (LogTypes class can be used).
            msg (str): The message showed to the user.
            is_internal (bool): Add the prefix if the log is internal to the compiler.
        """
        
        # Internal prefix
        if is_internal:
            prefix = Logger.LogTypes.C_PREFIX
        else:
            prefix = ""
            
        # DPC001
        print(f"[{prefix}] {log_type}: {msg}")
        