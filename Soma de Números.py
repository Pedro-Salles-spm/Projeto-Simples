contador = 1 
soma = 0 

while contador <= 5:
# recenbendo o numero na repetição para não pricisar declarar 5 variáveis 
     num = int(input('digite um numero:'))
     #somando todo numero que o usuario digitar 
     soma = soma + num
    
     contador = contador + 1
print ('A soma é:', soma)