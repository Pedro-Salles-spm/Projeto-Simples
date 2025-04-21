lado1 = int(input("digite o primriro lado:"))
lado2 = int(input("digite o segundo lado:"))
lado3 = int(input("digite o terceiro lado:"))

if lado1 == lado2 == lado3:
   print("tiangulo é equílatero")
   
# or siguinifica (ou)
elif lado1 == lado2 != lado3 or lado2 == lado3 !=lado1 or lado1 == lado3 !=lado2:
    print("É um triangulo isósceles")
    
else:
    print('É um triangulo escaleno')
    
    