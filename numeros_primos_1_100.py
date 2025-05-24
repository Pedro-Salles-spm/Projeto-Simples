numeros = []

while True:
 print('\n----- menu inicial -----\n')
 print('\n1 - Mostrar numero prinmos entre 1 e 100')
 print('\n2 - Mostrar a quantidade de  numeros primos encontrados')
 print('\n3 - Sair')
 
 opcao = int(input('\n Digite uma opção:'))
 
 if opcao == 1:
        for divisor in range(1, 101): # for i in range significa que o lop vai percorrer de 1 a 100
            if divisor > 1:
                for testar in range(2, divisor):
                    if (divisor % testar) == 0:
                        break
                else:
                    numeros.append(divisor)
        print(f'\n Os numeros primos entre 1 e 100 são: {numeros}')
        
 elif opcao == 2:
     print(f'\n A quantidade de numeros primos encontrados é: {len(numeros)}') # len conta quantos elementos tem na lista
     
 elif opcao == 3:
        print('Saido do programa')
        
 else:
     print('Opçao inválida')
     
     
 
                    
        
        
        
     
    
     
 
 
 
 
