Minha resposta:
metros = float(input('Digite uma distancia em metros'))
Centimetros = metros * 100
Milimetros = metros * 1000
print(f'A Medida de {metros}m corresponde a: ')
print(f'{Centimetros:.0f}cm')
print(f'{Milimetros:.0f}mm')

RESOLUÇÃO
n1 = float (input('Digite um valor em metros'))
print ('{} metros equivale a {:.0f) centimetros e {:.0f) milimetros'.format(n1, n1*100, n1*1000))
