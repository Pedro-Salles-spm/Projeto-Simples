valor = int(input("dgite um valor:"))
valorju = int(input('digite o valor de juros:'))
valorano = int(input('valor de anos'))

montantef = valor +(valor * valorju * valorano /100)

print('montante final:',montantef)
