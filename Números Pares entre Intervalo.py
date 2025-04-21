
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio

atual = inicio + 1

print(f"Números pares entre {inicio} e {fim}:")

while atual < fim:
    if atual % 2 == 0:
        print(atual)
    atual += 1