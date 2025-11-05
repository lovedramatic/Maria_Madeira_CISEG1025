#Verficiar se o cheque pode ser descontado

saldo = float(input("Escreva o saldo atual [€]"))
cheque = float(input("Escreva o valor do cheque [€]"))

if cheque <= saldo: # so desconta se o saldo for suf // atualiza estado no -=
    saldo -= cheque
    print(f"Cheque descontado, o novo saldo é de: {saldo:.2f}€")
else:
    print(f"Cheque nao pode ser descontado, o saldo nao e suficiente")