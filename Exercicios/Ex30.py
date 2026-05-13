distancia = float(input("Qual é a distância da viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da sua passagem será R${preco:.2f}")
