Minha resposta:
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
pago_dias = dias * 60
pago_km = km * 0.15
total = pago_dias + pago_km
print(f'O total a pagar é de R${total:.2f}')
RESOLUÇÃO:
dias = int(input('Quantos dias alugados?'))
Km = float(input('Quantos Km rodados?'))
diaria = dias*60
percurso = Km * 0.15
custo diaria + percurso
print('o total a pagar é de R${:.2f}'.format(custo))
