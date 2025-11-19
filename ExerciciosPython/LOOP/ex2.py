count = 1

while count <= 10:
    num = int(input(f"Digite o {count}º número:"))

    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")
    count += 1