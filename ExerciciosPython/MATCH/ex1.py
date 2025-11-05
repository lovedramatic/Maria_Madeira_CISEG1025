dia=(input("Diga o dia da semana:"))

match dia:
    case "Segunda"|"Terça"|"Quarta"|"Quinta"|"Sexta":
        print("Dia útil")
    case "Sábado"|"Domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido. Digite um dia da semana válido.")