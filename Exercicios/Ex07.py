Minha resposta:
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é {d}.')
print(f'O triplo de {n} é {t}.')
print(f'A raiz quadrada de {n} é {r:.2f}.')

RESOLUÇÃO:
n1 = int (input ('Digite um número '))
print('o número digitado foi {} o seu dobro é {}, seu triplo {} e sua raiz quadrada é {:.2f}
'.format(n1, n1*2, n1*3, n1**0.5))
#para calcular a raiz quadrada posso utilizara função pow(n**0.5)
