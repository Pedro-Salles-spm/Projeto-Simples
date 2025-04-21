valor = int(input('Qual o valor do produto ?'))
desconto = int(input('Qual o desconto?'))

cd = valor /100 * desconto
vp = valor - cd 

if valor > 100:
   print('Valor com desconto:',vp)
   
else:
    print('Valor está abaixo')
   
   