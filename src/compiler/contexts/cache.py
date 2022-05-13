from . import Types

from typing import Dict, Any, List, Optional
from pathlib import Path


class Cache:
    class Compiler:
        """Compiler internal global cached variables."""
        
        # Globally stored compiler tree (List[Path])
        compiler_tree: Optional[List[Path]] = None
        
        # Data loaded from the compiler database directory
        # Generic YAML files used to store compiler data
        compiler_database: Dict[str, Any] = {
            "diagnostic_messages.yaml": None,
            "clua.config.yaml": None,
            "system.yaml": None
        }
        
        compiler_tokens: List[Types] = []


    class Project:
        """User project global cached variables."""
        
        # Globally stored user project tree (List[Path])
        project_tree: Optional[List[Path]] = None
        
        # Contains a list of all the clua file paths (sorted by directory depth)
        clua_trace: Optional[List[Path]] = []
        
        # Config file dicts loaded from the user project directory
        loaded_config_dicts: Optional[Dict[Path, Any]] = {}
        