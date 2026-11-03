
def build_diff(data1, data2):
    result = []
    data1_keys = data1.keys()
    data2_keys = data2.keys()

    all_keys = sorted(set(data1_keys) | set(data2_keys))

    for key in all_keys:
        if key in data1 and key not in data2:
            result.append({
                "key": key,
                "status": "removed",
                "value": data1[key]
            })
        elif key in data2 and key not in data1:
            result.append({
                "key": key,
                "status": "added",
                "value": data2[key]
            })

        elif isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
            result.append({
                "key": key,
                "status": "nested",
                "children": build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            result.append({
                "key": key,
                "status": "unchanged",
                "value": data1[key]
            })
        else:
            result.append({
                "key": key,
                "status": "changed",
                "old_value": data1[key],
                "new_value": data2[key]
            })

    return result
