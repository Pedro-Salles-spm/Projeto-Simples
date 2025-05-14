alunos = []

for i in range(5):
    nome = input('digite seu nome:')
    av1 = float(input('digite a nota da av1:'))
    av2 = float(input('digite a nota da av2:'))
    
    media = (av1 + av2) /2
    
    alunos.append({
        'nome': nome,
        'av1':av1,
        'av2': av2,
        'media': media
    })
    print('\n ----resultado final ----')
    
    for aluno in alunos:
        print(f'nome: {aluno['nome']}, - avaliação1: {aluno['av1']}, - avaliação2: {aluno['av2']}, - media: {aluno['media']:.2f}')