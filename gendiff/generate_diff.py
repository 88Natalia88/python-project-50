
from pathlib import Path

from gendiff.parser import parse

from gendiff.build_diff import build_diff

from gendiff.formatters.stylish import format_stylish

from gendiff.formatters.plain import format_plain

from gendiff.formatters.json_formatter import format_json

def read_file(file_path):
    path = Path(file_path)
    format_content = path.suffix[1:].lower()
    with open(file_path) as file:
        content = file.read()
    
    return parse(content, format_content)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff_tree = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
        
    raise ValueError(f"Unknown format: {format_name}")