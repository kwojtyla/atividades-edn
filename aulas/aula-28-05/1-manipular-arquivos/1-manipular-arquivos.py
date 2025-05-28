import os
from filekits import csvkit as csv, txtkit as txt, jsonkit as json

def get_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def show_data(data):
    for person in data:
        print(f"Nome: {person['Nome']}, Idade: {person['Idade']}, Cidade: {person['Cidade']}")

def main():
    path = input("Digite o caminho do arquivo: ").strip()
    
    if not os.path.exists(path):
        print("Arquivo não encontrado.")
        return

    extension = get_extension(path)

    if extension == '.txt':
        data = txt.read(path)
    elif extension == '.csv':
        data = csv.read(path)
    elif extension == '.json':
        data = json.read(path)
    else:
        print("Formato de arquivo não suportado.")
        return

    print("\nConteúdo do arquivo:")
    show_data(data)

    while True:
        option = input("\nDeseja adicionar uma nova pessoa? (s/n): ").lower()
        if option == 's':
            name = input("Nome: ")
            age = input("Idade: ")
            city = input("Cidade: ")
            data.append({'Nome': name, 'Idade': age, 'Cidade': city})

            if extension == '.txt':
                txt.write(path, data)
            elif extension == '.csv':
                csv.write(path, data)
            elif extension == '.json':
                json.write(path, data)

            print("\nDados atualizados com sucesso!")
            show_data(data)
        else:
            break
    
    print("\nConteúdo do arquivo:")
    show_data(data)

if __name__ == '__main__':
    main()
