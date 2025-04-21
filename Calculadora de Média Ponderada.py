nota1 = int(input('digite a primeira nota:'))
peso1 = int(input('digite o primeiro peso:'))

nota2 = int(input('digite a segunda nota:'))
peso2 = int(input('digite o segunda peso:'))

nota3 = int(input('digite a terceiro nota:'))
peso3 = int(input('digite o terceiro peso:'))


rt = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
mediaponderada= rt / (peso1 + peso2 + peso3)

print("méidia ponderada:",mediaponderada)
