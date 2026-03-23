Minha resposta:
preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
preco_final = preco - desconto
print(f"O preço com 5% de desconto é: R$ {preco_final:.2f}")

RESOLUÇÃO:
preco = float(input('Qual é o preço do produto? R$'))
desconto = preco (preco * 5 / 100)
print('o produto que custava{:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))
