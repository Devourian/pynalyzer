from pathlib import Path
from typing import Callable
from unittest.mock import MagicMock, patch

import pytest

from pynalyzer.configuration_parsing.configuration_path_finder import (
    ConfigurationPathFinder,
)
from pynalyzer.utils.constants import CONFIGURATION_FILE_NAME
from pynalyzer.utils.exceptions import ConfigurationNotFoundError


class TestConfigurationPathFinder:
    __CONFIGURATION_PATH = Path.home() / CONFIGURATION_FILE_NAME
    __CONFIGURATION_FILE_PATH = __CONFIGURATION_PATH
    __DIRECTORY_WITH_SAME_NAME_AS_CONFIG_FILE = __CONFIGURATION_PATH

    def setup_method(self, method: Callable) -> None:
        if method.__name__ == "test_find_raises_is_directory_error":
            self.__DIRECTORY_WITH_SAME_NAME_AS_CONFIG_FILE.mkdir()

        if method.__name__ == "test_find_passes":
            self.__CONFIGURATION_FILE_PATH.touch()

    def teardown_method(self, method: Callable) -> None:
        if method.__name__ == "test_find_raises_is_directory_error":
            self.__DIRECTORY_WITH_SAME_NAME_AS_CONFIG_FILE.rmdir()

        if method.__name__ == "test_find_passes":
            self.__CONFIGURATION_FILE_PATH.unlink()

    @patch.object(Path, "cwd", return_value=Path.home())
    def test_find_raises_is_directory_error(
        self,
        _path_cwd_mock: MagicMock,
    ) -> None:
        EXPECTED_ERROR_MESSAGE = (
            "pyproject.toml is a directory, but should be a proper TOML file"
        )

        with pytest.raises(expected_exception=IsADirectoryError) as exception_info:
            ConfigurationPathFinder.find()

        assert str(exception_info.value) == EXPECTED_ERROR_MESSAGE

    @patch.object(Path, "cwd", return_value=Path.home())
    def test_find_raises_file_not_found_error(
        self,
        _path_cwd_mock: MagicMock,
    ) -> None:
        EXPECTED_ERROR_MESSAGE = (
            "Couldn't find pyproject.toml configuration"
            " file in current working directory"
        )

        with pytest.raises(
            expected_exception=ConfigurationNotFoundError
        ) as exception_info:
            ConfigurationPathFinder.find()

        assert str(exception_info.value) == EXPECTED_ERROR_MESSAGE

    @patch.object(Path, "cwd", return_value=Path.home())
    def test_find_passes(
        self,
        _path_cwd_mock: MagicMock,
    ) -> None:
        expected_configuration_file_path = Path.home() / CONFIGURATION_FILE_NAME

        try:
            configuration_file_path = ConfigurationPathFinder.find()
        except Exception as any_exception:
            pytest.fail(
                f"ConfigurationPathFinder.find raised [{type(any_exception)}: "
                f"{any_exception}] unexpectedly!"
            )

        assert configuration_file_path == expected_configuration_file_path
