notas = []

print("Digite as notas dos alunos (de 0 a 10). Para encerrar, digite 'fim'.")

while True:
    entrada = input("Informe a nota: ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido ou 'fim' para encerrar.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nForam registradas {len(notas)} notas.")
    print(f"Média da turma: {round(media, 2)}")
else:
    print("\nNenhuma nota válida foi registrada.")