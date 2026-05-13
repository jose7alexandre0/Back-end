distancia = float(input("Qual é a distância da viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da sua passagem será R${preco:.2f}")

Resolução
viagem = float(input("Qual é a distância da sua viagem?"))
curta = 0.5 * viagem
longa = 0.45 * viagem
print("Você está prestes a começar uma viagem de {} Km".format(viagem))
if viagem <=200: print("E o preço da sua passagem será de R${}".format(curta))
else:
    print("E o preço da sua passagem será de R${:.2f}".format(longa))
