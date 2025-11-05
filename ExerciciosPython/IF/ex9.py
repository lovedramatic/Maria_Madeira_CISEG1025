#Nome do mes de 1 a 12

n= int(input("Digite um número de 1 a 12: "))
m = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}
print(m.get(n, "Número inválido!"))

# .get -- procura chave no dicionario -- se encontrar devolver n, senao, devolve valor padrao(nr invalido)