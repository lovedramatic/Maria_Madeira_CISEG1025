#Desconto de compra

nome = input("Nome do cliente: ")
compra = float(input("Valor da compra (€): "))

if compra <= 200:
    desconto = 0.10
elif compra <= 500:
    desconto = 0.15
else:
    desconto = 0.20

valor_desconto = compra * desconto
total = compra - valor_desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {valor_desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")
