import os
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from textsummerizer.logging import logger
from typing import List, Optional, Any
from pathlib import Path
import yaml
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        e: raises exception if yaml file is not found

    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path like input

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024, 2)
    return f"{size_in_kb} KB"