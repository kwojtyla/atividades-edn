import json

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)