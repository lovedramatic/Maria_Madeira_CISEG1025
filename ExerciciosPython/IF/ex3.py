#Mostrar numeros em ordem crescente e descrecente

n1 = int(input("Escreva o 1o nr:"))
n2 = int(input("Escreva o 2o nr:"))

if n1 < n2:
    print("Crescente:", n1, "-", n2)
else:
    print("Crescente:", n2, "-", n1)

if n1 > n2:
    print("Descrescente:", n1, "-", n2)
else:
    print("Decrescente:", n2, "-", n1)