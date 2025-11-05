#Media de 10 notas + contar quantas >= média

notas = []
for i in range(10): # pede 10 leituras/valores
    n = float(input(f"Nota {i+1}: "))
    if n < 0 or n > 20:
        print("Nota fora de 0 a 20. Ajustada.")
        n = max(0, min(20, n))
    notas.append(n)

med = sum(notas) / len(notas)
acima_ou_igual = sum(1 for n in notas if n >= med)

print(f"Média da turma: {med:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_ou_igual}")
