frase = input("Digite uma frase:")

match frase:
    case "Olá" | "Ola" | "Bom Dia":
        print("Saudação")
    case frase if frase.endswith("?"):
        print("Pergunta")
    case frase if "Tchau" in frase or "Adeus" in frase:
        print("Despedida")
    case _:
        print("Mensagem genérica")