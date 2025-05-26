pares = 0
impares = 0

print("Digite números inteiros. Para encerrar, digite 'fim'.")

while True:
    entrada = input("Número: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("Esse número é par.")
            pares += 1
        else:
            print("Esse número é ímpar.")
            impares += 1

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

print("\nResumo:")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")