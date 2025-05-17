funcionarios = []


for i in range(5):
    print('----- Menu Do Fucionario -----')
    print('\n 1 - Cadastrar funcionario ')
    print('\n 2 - Explicação do calculo ')
    print('\n 3 - ver funcionarios cadastrados')
    print('\n 4 - Sair\n')
    
    
    
    opcao = int(input('Escolha uma opção:'))
    
    
 
    if opcao == 1:
        
        print('\n----- Cadastro do Funcionario------\n')
        
        nome = input('Digite seu nome:')
    
        dia_trabalhado = int(input('\nDigite o numero de dias trabalhados:'))
    
        valor_da_hora = float(input('\nDigite o valor da hora:'))
    
        horas_trabalhadas = float(input('\nDigite o numero de horas trabalhadas:'))
        
        salario = (horas_trabalhadas * valor_da_hora) * dia_trabalhado
        
        print (f'\n Funcionario {nome} cadastrdo com sucesso. \n')
        
    elif opcao == 2:
        print('\n----- Explicação do calculo ------\n')
        print('\nO salario é calculado da seguinte forma:\n')
        print('\n As horas trabalhadas multiplicadas pelo valor da hora, multiplicado pelo numero de dias trabalhados')
        print(' Exemplo: 10 horas trabalhadas * 10 reais * 5 dias trabalhados = 500 reais\n')
              
    elif opcao == 3:
        funcionarios.append([nome,dia_trabalhado, valor_da_hora, horas_trabalhadas,salario])
        print('\n Resutado abaixo \n')
    
        for funcionario in funcionarios:
             print(f'Ola {funcionario[0]} você trabalhou {funcionario[1]} dias, com o valor da hora de {funcionario[2]} reais, e trabalhou {funcionario[3]} horas, e seu salario é de {funcionario[4]:,.2f} reais')
    
    elif opcao == 4:
        print('saindo do siatema ...')
        break
    else:
        print('Opção invalida, tente novamente')
        continue
       
    
    
    
    
    
    
   
      
    
    
    
    
    