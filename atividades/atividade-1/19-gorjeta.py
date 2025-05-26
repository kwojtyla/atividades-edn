
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    try:
        if valor_conta < 0 or porcentagem_gorjeta < 0:
            print("Erro: Valores negativos não são permitidos.")
            return None
        if valor_conta == 0:
            print("A conta está zerada. Nenhuma gorjeta será calculada.")
            return 0.0

        gorjeta = valor_conta * (porcentagem_gorjeta / 100)
        return gorjeta

    except Exception as erro:
        print("Erro ao calcular a gorjeta:", erro)
        return None

try:
    valor = float(input("Digite o valor da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
    valor_gorjeta = calcular_gorjeta(valor, porcentagem)

    if valor_gorjeta is not None:
        print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")