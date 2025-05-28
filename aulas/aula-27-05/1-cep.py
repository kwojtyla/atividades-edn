import requests

def get_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if "erro" in data:
            print("❌ CEP não encontrado.")
            print(data)
        else:
            print(f"\n✅ Endereço encontrado:")
            print(f"Logradouro: {data.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {data.get('bairro', 'Não disponível')}")
            print(f"Cidade: {data.get('localidade', 'Não disponível')}")
            print(f"Estado: {data.get('estado', 'Não disponível')}\n")
    except requests.RequestException as e:
        print("❌ Erro ao conectar com o ViaCEP:", e)


cep = input("Digite um CEP (somente números): ").strip()
if not cep.isdigit() or len(cep) != 8:
    print("❌ CEP inválido. Ele deve conter exatamente 8 dígitos numéricos.")
get_cep(cep)
