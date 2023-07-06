from pathlib import Path

from pynalyzer.utils.constants import CONFIGURATION_FILE_NAME


class ConfigurationNotFoundError(Exception):
    def __init__(self) -> None:
        error_message = (
            f"Couldn't find {CONFIGURATION_FILE_NAME} configuration"
            f" file in current working directory"
        )
        super().__init__(error_message)


class ConfigurationSectionNotFoundError(Exception):
    def __init__(self, configuration_file_path: Path) -> None:
        error_message = (
            f"[tool.pynalyzer] section was not found in "
            f"{configuration_file_path} configuration file"
        )
        super().__init__(error_message)


class ConfigurationAttributeNotFoundError(Exception):
    def __init__(
        self,
        attribute_name: str,
    ) -> None:
        error_message = (
            f"{attribute_name} attribute was not found "
            f"under [tool.pynalyzer] section in configuration file"
        )
        super().__init__(error_message)
