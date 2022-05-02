class Cache:
    class Compiler:
        # Global accessed data
        data = {
            "default_config": None,
            "diagnostic_messages": None
        }
        
        # Central tree (paths list of the available compiler data) 
        tree = None


    class Project:
        directory_tree = []
        config_files_tree = []
    