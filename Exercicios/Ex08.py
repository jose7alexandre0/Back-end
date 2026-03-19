Minha resposta:
Nota1 = float(input('digite a primeira nota'))
Nota2 = float(input('Digite a segunda nota'))
media = (Nota1 + Nota2) / 2
print(f"\nNota 1: {Nota1}")
print(f"Nota 2: {Nota2}")
print(f"Média Final: {media:.1f}")

RESOLUÇÃO
n1= float(input('Digite a primeira nota '))
n2= float(input('Digite a segunda nota '))
print('A media entre {:.2f}, e {:.2f} é {:.2f}'.format(n1, n2, (n1+n2)/2))
