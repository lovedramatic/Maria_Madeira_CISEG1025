soma = 0
div = 1
num = int(input("Insira um número: "))

while div <= num:
    if num % div == 0:
        soma += 1
    div += 1
print(f"O número tem {soma} divisores.")