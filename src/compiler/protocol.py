class Protocol:
    class Register:
        file_id = 0
        file_path = None
        
        instruction = {
            "instruction_type": None,
            "line_number": None
        }
    

    class Tokens:
        pass
    
    
    class InstructionTypes:
        PASS = {}
        
        CLOSE_FILE = {}
