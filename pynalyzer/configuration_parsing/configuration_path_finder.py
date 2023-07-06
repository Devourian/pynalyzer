from pathlib import Path

from pynalyzer.utils.constants import CONFIGURATION_FILE_NAME
from pynalyzer.utils.exceptions import ConfigurationNotFoundError


class ConfigurationPathFinder:
    @staticmethod
    def find() -> Path:
        configuration_file_path = Path.cwd() / CONFIGURATION_FILE_NAME
        ConfigurationPathFinder.__validate_path(
            configuration_file_path=configuration_file_path
        )

        return configuration_file_path

    @staticmethod
    def __validate_path(configuration_file_path: Path) -> None:
        if not configuration_file_path.exists():
            raise ConfigurationNotFoundError

        if configuration_file_path.is_dir():
            raise IsADirectoryError(
                "pyproject.toml is a directory, but should be a proper TOML file"
            )
