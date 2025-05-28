import csv

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write(path, data):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        fields = ['Nome', 'Idade', 'Cidade']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)