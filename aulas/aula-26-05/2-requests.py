import requests

def get_profile():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]

        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        country = user['location']['country']

        print("=== Perfil de Usuário Gerado ===")
        print(f"Nome: {name}")
        print(f"E-mail: {email}")
        print(f"País: {country}")
    else:
        print("Erro ao obter dados da API.")

get_profile()
