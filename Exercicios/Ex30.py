velocidade = float(input("Qual a velocidade atual do carro em km/h? "))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"MULTADO! Você excedeu o limite de 80km/h.")
    print(f"O valor da multa é de R${multa:.2f}.")
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
