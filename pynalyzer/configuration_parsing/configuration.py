from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


@dataclass(frozen=True)
class Configuration:
    config_file_path: Path
    paths_to_analyze: Tuple[Path, ...]
