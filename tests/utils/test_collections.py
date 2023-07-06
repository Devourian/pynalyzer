from pathlib import Path

import pytest

from pynalyzer.utils.converters import PathCollection, convert_path_collection_to_string


class TestCollections:
    @pytest.mark.parametrize(
        "path_collection, expected_result",
        [
            (set(), ""),
            ([Path("src")], "src"),
            (
                (
                    Path("/home/user/some_file.py"),
                    Path("some_dir"),
                ),
                "/home/user/some_file.py some_dir",
            ),
        ],
    )
    def test_convert_path_collection_to_string(
        self,
        path_collection: PathCollection,
        expected_result: str,
    ) -> None:
        assert convert_path_collection_to_string(path_collection) == expected_result
