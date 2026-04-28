Minha resposta:
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

RESOLUÇÃO
from random import choice
aluno1 = str (input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str (input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice (lista) #escolhe um da lista
print('o aluno escolhido foi {}'.format(escolhido))
