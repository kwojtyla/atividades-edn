from datetime import datetime

def calcula_idade(anoNascimento):    
    anoAtual = datetime.now().year
    idadeEmDias = (anoAtual - anoNascimento) * 365
    return idadeEmDias

try: 
    idade = int(input("Digite o seu ano de nascimento: "))

    if idade <= 0:
        print("Ano inválido! Digite um valor positivo.")
    else:
        idadeEmDias = calcula_idade(idade)
        print("Você tem aproximadamente", idadeEmDias, "dias de vida.")

except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro para o ano de nascimento.")