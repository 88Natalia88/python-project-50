
from pathlib import Path

from gendiff.parser import parse

def read_file(file_path):
    path = Path(file_path)
    format_content = path.suffix[1:].lower()
    with open(file_path) as file:
        content = file.read()
    
    return parse(content, format_content)


def generate_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    
    result = []
    data1_keys = data1.keys()
    data2_keys = data2.keys()

    all_keys = sorted(set(data1_keys) | set(data2_keys))

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {generate_str(data1[key])}")
        elif key in data2 and key not in data1:
            result.append(f"  + {key}: {generate_str(data2[key])}")
        elif key in data1 and key in data2 and data1[key] == data2[key]:
            result.append(f"    {key}: {generate_str(data1[key])}")
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            # result.append(f"  - {key}: {generate_str(data1[key])}")
            # result.append(f"  + {key}: {generate_str(data2[key])}")
            result.extend((f"  - {key}: {generate_str(data1[key])}", 
                           f"  + {key}: {generate_str(data2[key])}"))

    return "{\n" + "\n".join(result) + "\n}"


