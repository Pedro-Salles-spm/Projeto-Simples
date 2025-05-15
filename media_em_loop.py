alunos = []

for i in range(5):
    nome = input('digite seu nome:')
    av1 = float(input('\ndigite a nota da av1:'))
    av2 = float(input('\ndigite a nota da av2: '))
    print('\n')
    
    media = (av1 + av2) /2
    
    if media >= 6:
        print(f'parabens {nome},vecê foi aprovado com a media {media:.2f}')
        
    else:
        print(f'Que pena {nome}, você foi reprovamdo com a media {media:.2f}')
        
    alunos.append([nome,av1,av2,media])
    print('\n ----resultado final---- \n')
    
    for aluno in alunos:
        
      if aluno[3] >= 6:
        print(f'nome: {aluno[0]}, - avaliação1: {aluno[1]}, - avaliação2: {aluno[2]}, - media: {aluno[3]:.2f} - aprovado')
      else:
        print(f'nome: {aluno[0]}, - avaliação1: {aluno[1]}, - avaliação2: {aluno[2]}, - media: {aluno[3]:.2f} - reprovado')