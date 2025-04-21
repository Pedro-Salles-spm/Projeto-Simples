
n = int(input("Digite quantos números da sequência de Fibonacci você quer ver: "))


a = 0
b = 1


contador = 0

print("Sequência de Fibonacci:")


while contador < n:
    print(a, end=' ')  
    proximo = a + b    
    a = b              
    b = proximo
    contador += 1      
