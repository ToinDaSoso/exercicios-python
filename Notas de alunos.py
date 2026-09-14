alunos = {
    'Ana': [8,7,9],
    'Bruno': [5,6,4],
    'Carlos': [10,9,8]
}

for aluno in alunos:
    soma_notas = sum(alunos[aluno])
    media = soma_notas/len(alunos[aluno])
    if media>=7:
        print(f'{aluno}: {media} - Aprovado')
    else:
        print(f'{aluno}: {media} - Reprovado')