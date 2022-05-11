class Cache:
    class Compiler:
        """Compiler internal global cached variables."""
        
        # Globally stored compiler tree (list[Path])
        compiler_tree = None
        
        # Data loaded from the compiler data directory
        # Generic YAML files used to store config/messages
        loaded_data = {
            "diagnostic_messages.yaml": None,
            "clua.config.yaml": None
        }


    class Project:
        """User project global cached variables."""
        
        # Globally stored user project tree (list[Path])
        project_tree = None
        
        # Contains a list of all the clua file paths (sorted by directory depth)
        clua_files = []
        
        # Config files loaded from the user project directory
        loaded_configs = {}
        