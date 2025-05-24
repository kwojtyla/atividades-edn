try:
    ano = int(input("Digite um ano: "))

    if ano <= 0:
        print("Ano inválido! Digite um valor positivo.")
    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro para o ano.")