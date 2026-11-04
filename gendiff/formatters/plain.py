def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def make_plain_lines(diff, current_path=""):
    result = []
    
    for item in diff:
        key = item['key']
        status = item['status']
        
        property_path = f"{current_path}.{key}" if current_path else key

        if status == "added":
            val = stringify(item['value'])
            result.append(f"Property '{property_path}' 
                          was added with value: {val}")

        elif status == "removed":
            result.append(f"Property '{property_path}' was removed")

        elif status == "changed":
            val_old = stringify(item['old_value'])
            val_new = stringify(item['new_value'])
            result.append(
                f"Property '{property_path}' was updated. 
                From {val_old} to {val_new}"
            )

        elif status == "nested":
            child_lines = make_plain_lines(item['children'], property_path)
            result.extend(child_lines)

    return result


def format_plain(diff):
    lines = make_plain_lines(diff)
    return "\n".join(lines)

