#Identificar numeros pares e impares

par = 0
imp = 0

for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    if n % 2 == 0:
        par += 1
    else:
        imp += 1

print(f"Pares: {par}")
print(f"Ímpares: {imp}")