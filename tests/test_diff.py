from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_diff_json():
    path_json1 = get_test_data_path('filepath1.json')
    path_json2 = get_test_data_path('filepath2.json')

    actual = generate_diff(path_json1, path_json2)
    expected = read_file("expected.txt").strip()

    assert actual == expected
