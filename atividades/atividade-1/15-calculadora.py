while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = num1 / num2
        else:
            print("Erro: Operação inválida. Use apenas +, -, * ou /.")
            continue

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break 

    except ValueError:
        print("Erro: Por favor, insira números válidos.")