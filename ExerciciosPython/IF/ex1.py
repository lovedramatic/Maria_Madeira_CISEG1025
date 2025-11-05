#Converter segundos em horas minutos e segundos

s = int(input("Digite o total em segundos:"))
h = s //3600
r = s % 3600
m = r // 60
sfinal = r % 60

print(f"{h} horas, {m} minutos e {sfinal} segundos!") 