nome = input("Insira o nome completo: ")
valido = True

for i in range(len(nome)):
    ch = nome[i]
    codigo = ord(ch)
    if 65 <= codigo <= 90:
        pass
    elif 97 <= codigo <= 122:
        pass
    elif codigo == 32:
        pass
    else:
        print("INVÁLIDO - nome contém caracteres não permitidos.")
        valido = False
        break
    if i == 0:
        if not (65 <= codigo <= 90):
            print("INVÁLIDO - primeira letra do nome não é maiúscula.")
            valido = False
            break
    if nome[i - 1] == " ":
        if not (65 <= codigo <= 90):
            print("INVÁLIDO - letra após espaço não é maiúscula.")
            valido = False
            break
if valido:
    print("Nome válido!")
