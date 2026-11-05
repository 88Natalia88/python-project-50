def generate_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return format_dict(value, depth)
    return str(value)


def format_dict(value, depth):
    lines = ["{"]
    indent = " " * ((depth + 1) * 4)
    closing_indent = " " * (depth * 4)

    for k, v in value.items():

        lines.append(f"{indent}{k}: {generate_str(v, depth + 1)}")

    lines.append(f"{closing_indent}" + '}')
    return "\n".join(lines)


def format_nodes(diff, depth):
    result = []
    indent = " " * (depth * 4)
    sign_indent = " " * (depth * 4 - 2)

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "removed":
            value_str = generate_str(item["value"], depth)
            result.append(f"{sign_indent}- {key}: {value_str}")

        elif status == "added":
            value_str = generate_str(item["value"], depth)
            result.append(f"{sign_indent}+ {key}: {value_str}")

        elif status == "unchanged":
            value_str = generate_str(item["value"], depth)
            result.append(f"{indent}{key}: {value_str}")

        elif status == "changed":
            old_str = generate_str(item["old_value"], depth)
            new_str = generate_str(item["new_value"], depth)
            result.extend((f"{sign_indent}- {key}: {old_str}", 
                           f"{sign_indent}+ {key}: {new_str}"))

        elif status == "nested":
            result.append(f"{indent}{key}: " + "{")
            result.extend(format_nodes(item["children"], depth + 1))
            result.append(f"{indent}" + "}")

    return result


def format_stylish(diff):
    inner_lines = format_nodes(diff, depth=1)
    return "{\n" + "\n".join(inner_lines) + "\n}"
