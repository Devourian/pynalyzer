from pathlib import Path
from typing import Collection, TypeVar

PathCollection = TypeVar("PathCollection", bound=Collection[Path])


def convert_path_collection_to_string(
    path_collection: PathCollection,
) -> str:
    paths_str = " ".join([str(path) for path in path_collection])
    return paths_str
