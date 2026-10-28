import pytest

from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.mark.parametrize("extension", ["json", "yml", "yaml"])
def test_generate_diff(extension):
    path1 = get_test_data_path(f'filepath1.{extension}')
    path2 = get_test_data_path(f'filepath2.{extension}')

    actual = generate_diff(path1, path2)
    expected = read_file("expected.txt").strip()

    assert actual == expected