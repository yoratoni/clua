from typing import Dict, Any, Optional
from pathlib import Path


class Cache:
    class Compiler:
        """Compiler internal global cached variables."""
        
        # Globally stored compiler tree (list[Path])
        compiler_tree: Optional[list[Path]] = None
        
        # Data loaded from the compiler data directory
        # Generic YAML files used to store config/messages
        compiler_data: Dict[str, Any] = {
            "diagnostic_messages.yaml": None,
            "clua.config.yaml": None
        }


    class Project:
        """User project global cached variables."""
        
        # Globally stored user project tree (list[Path])
        project_tree: Optional[list[Path]] = None
        
        # Contains a list of all the clua file paths (sorted by directory depth)
        clua_trace: Optional[list[Path]] = []
        
        # Config file dicts loaded from the user project directory
        loaded_config_dicts: Optional[Dict[Path, Any]] = {}
        