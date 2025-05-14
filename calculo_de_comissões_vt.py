# criar uma lista vazia que irá armazenar os da dodos das comissões dos funcionairios
comissoes = []

# loop que, nesse caso, roda apenas 1 vez (podderia ser aumentado prafor mais de um funcionário)
for i in range(1):
    # solicitar o nome do funcionario
    nome = input('digite seu nome:')
    # solicitar da comissão
    comissao = float(input('Digite o valor da comissão:'))
    # solicitar a comissão do segundo mes
    comissao2 = float(input('digite o valor da segunda comissão:'))
    
    #calculo da média 
    media = (comissao + comissao2) /2
    
    # adicionar o nome e a média na lista de comissões
    
    comissoes.append({
        'nome': nome,
        'comissao': comissao,
        'comissao2': comissao2,
        'media': media
    })
# imprimir a lista de comissões
print('\n ---- resultado final ----')
for comissao in comissoes:
    print(f" {comissao['nome']} - comissão 1: {comissao['comissao']}, comissão 2: {comissao['comissao2']}, média: {comissao['media']:.2f}")
    