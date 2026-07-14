tentativas_login = [3, 1, 14, 2, 28, 1, 9]

suspeitos = []

for tentativa in tentativas_login:
    if tentativa >= 8:
        suspeitos.append(tentativa)

print("Suspeitos:", suspeitos)
print("Quantidade:", len(suspeitos))
print("Pior caso:", max(suspeitos))
