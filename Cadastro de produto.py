
while True: 
    print('escolha uma opção:')
    
    print('1 - cadastrar produto.')
    
    print('2 -ver cadastro do produto.')
    
    print('3 - sair.')
    
    opçao = int(input('escolha uma opeção:'))
    
    if opçao == 1: 
        nome = input('digite o nome do pruduto:')
        
        preço = float(input('digite o preço do produto:'))
        
        print('produto cadastrado com sucesso!')
        
    elif opçao == 2:
        print(f'produto cadastrado: {nome}')
        
        print(f'preço do produto {preço}')
        
    elif opçao == 3:
        print('saindo...')
        break
    else:
        print('opção invalida!')
        
        