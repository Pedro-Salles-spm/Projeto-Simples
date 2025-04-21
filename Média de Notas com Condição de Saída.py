
soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota (ou um número negativo para sair): "))
    
    if nota < 0:
        break  
    
    soma += nota
    quantidade += 1


if quantidade > 0:
    media = soma / quantidade
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")
