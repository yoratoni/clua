class Cache:
    class Compiler:
        # Globally stored compiler tree
        compiler_tree = None
        
        # Data loaded from the compiler data directory
        # Generic YAML files used to store config/messages
        loaded_data = {
            "diagnostic_messages.yaml": None,
            "clua.config.yaml": None
        }


    class Project:
        # Globally stored user project tree
        project_tree = None
        
        # Config files loaded from the user project directory
        loaded_configs = {}
