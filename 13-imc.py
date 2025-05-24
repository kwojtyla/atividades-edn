# Calculadora de IMC

try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos.")
    else:
        imc = peso / (altura ** 2)
        
        print(f"Seu IMC é {imc:.1f}")
        
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        elif imc < 35:
            print("Classificação: Obesidade Grau I")
        elif imc < 40:
            print("Classificação: Obesidade Grau II")
        else:
            print("Classificação: Obesidade Grau III (mórbida)")

except ValueError:
    print("Entrada inválida! Por favor, digite números válidos para peso e altura.")
