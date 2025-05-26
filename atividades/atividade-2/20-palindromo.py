def valida_palindromo(texto):
    try:
        texto_formatado = ''.join(
            letra.lower() for letra in texto if letra.isalnum()
        )
        if texto_formatado == texto_formatado[::-1]:
            return "Sim"
        else:
            return "Não"
    except Exception as erro:
        print("Erro ao verificar palíndromo:", erro)
        return "Erro"

frase = input("Digite uma palavra ou frase: ")
resultado = valida_palindromo(frase)
print("É palíndromo?", resultado)