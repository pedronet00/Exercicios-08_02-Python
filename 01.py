def status_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4 and media < 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"



media = float(input("Insira a média do aluno: "))
status = status_aluno(media)
print(status) # Imprime "Aprovado"
