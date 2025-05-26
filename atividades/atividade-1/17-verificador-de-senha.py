print("Digite uma senha forte (mínimo 8 caracteres e pelo menos 1 número).")
print("Digite 'sair' para encerrar.")

while True:
    
    senha = input("Senha: ")

    if senha.lower() == 'sair':
        print("Encerrando o verificador de senhas.")
        break

    if len(senha) < 8:
        print("Senha fraca: precisa ter pelo menos 8 caracteres.")
        continue

    tem_numero = False
    for caractere in senha:
        if caractere >= '0' and caractere <= '9':
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca: precisa conter pelo menos um número.")
        continue

    print("Senha forte! Cadastro aceito.")
    break

    
