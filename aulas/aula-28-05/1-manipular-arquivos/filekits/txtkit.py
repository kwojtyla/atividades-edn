def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        rows = f.readlines()
        data = []
        for row in rows:
            name, age, city = row.strip().split(',')
            data.append({'Nome': name, 'Idade': age, 'Cidade': city})
        return data

def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        for person in data:
            f.write(f"{person['Nome']},{person['Idade']},{person['Cidade']}\n")