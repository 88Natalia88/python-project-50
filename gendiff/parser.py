import json

import yaml

def parse(content, format_content):
    if format_content == 'json':
        return json.loads(content)
    elif format_content in ('yaml', 'yml'):
        return yaml.safe_load(content)