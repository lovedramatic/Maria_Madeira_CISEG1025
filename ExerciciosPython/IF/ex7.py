#Media de nota com pesos (2, 3 e 5)

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

med = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print(f"Média: {med:.1f}")

if med >= 6:
    print("Aprovado")
else:
    print("Reprovado")
