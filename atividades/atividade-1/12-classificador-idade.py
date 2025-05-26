try:
    idade = int(input("Digite sua idade: "))
    
    if idade < 0:
        print("Idade inválida! Não pode ser negativa.")
    elif idade <= 12:
        print("Você é uma Criança.")
    elif idade <= 17:
        print("Você é um Adolescente.")
    elif idade <= 59:
        print("Você é um Adulto.")
    else:
        print("Você é um Idoso.")
        
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")