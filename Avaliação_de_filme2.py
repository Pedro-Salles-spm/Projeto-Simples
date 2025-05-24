dados = []

for i in range(3):
    nome = input('Digite seu nome: ')
    nome_do_filme = input('Digite o nome do filme: ')

    # Verifica se o nome e o nome do filme estão vazios
    if nome.strip() == '' or nome_do_filme.strip() == '':
        print('O nome e o nome do filme não podem estar vazios.\n')
        continue

    # Verifica se há números no nome ou no nome do filme
    if any(char.isdigit() for char in nome) or any(char.isdigit() for char in nome_do_filme):
        print('O nome e o nome do filme não podem conter números.\n')
        continue

    try:
        nota = float(input('Digite a nota do filme: '))

        if 0 <= nota <= 10:
            
            dados.append([nome, nome_do_filme, nota])
            print('\n--- Dados cadastrados ---\n')
        else:
            print('A nota deve ser entre 0 e 10.\n')

    except ValueError:
        print('A nota deve ser um número válido.\n')

# Exibir os dados cadastrados
print("\n--- Resultados ---\n")
for dado in dados:
    print(f'Nome: {dado[0]} - Nome do filme: {dado[1]} - Nota: {dado[2]}')