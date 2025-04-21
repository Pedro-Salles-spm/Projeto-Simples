numeroReal = 10 
numeroAleatorio = int(input("digite um numero:"))


while numeroAleatorio != numeroReal:
    print("Nao é esse numero")
    
    if numeroAleatorio <= 5:
        print("dica é maior que 5")
        
    elif numeroAleatorio == 9:
        print("Na trave!!!")
           
    elif numeroAleatorio >= 11:
        print("Mais pra baixo")
           
    numeroAleatorio = int(input("digite outro numero:"))
        
print('vocé acertou!')   

    