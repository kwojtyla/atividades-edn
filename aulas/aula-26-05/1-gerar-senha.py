import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Digite o número de caracteres da senha: "))

    if tamanho <= 0:
        print("O tamanho deve ser maior que zero.")
        
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")