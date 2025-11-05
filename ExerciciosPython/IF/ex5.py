#Ler 3 valores e exibir ordem crescente e decrescente

n1 = int(input("1o numero:"))
n2 = int(input("2o numero:"))
n3 = int(input("3o numero:"))

lista = [n1, n2, n3]

lista.sort()
print("Crescente:", lista)
lista.reverse()
print("Decrescente:", lista)