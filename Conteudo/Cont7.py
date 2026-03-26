MÓDULOS EM PYTHON
Para importar bibliotecas e funcionalidades em Python utiliza-se o comando Import seguido do nome da biblioteca ou módulo que ira ser carregado nesse programa.
Para importar coisa específicas de uma bibllioteca utiliza-se o comando from seguido do nome da biblioteca seguido da palavra import seguido do item que deseja importar.

BIBLIOTECA MATH
Essa biblioteca e bem utilizada no Python e seu nome significa matemática.
Quando importada ela traz diversos recursos matemáticos como por exemplo a funcionalidade ceil que arredonda números pra cima ou a funcionalidade floor que realiza o arredondamento pra baixo.
BIBLIOTECA MATH
A funcionalidade trunc, elimina números da virgula pra frente.
A funcionalidade pow é usada para a exponenciação, semelhante ao uso de 2 asteríscos.
A funcionalidade sqrt utilizada para calcular a raiz quadrada
A funcionalidade factorial calcula o fatorial de um número
Ex: import math (importa tudo para o programa).
From math import sqrt, ceil(importa apenas a funcionalidade sqrt e a ceil).

import math
num = int(input('Digite um número: ' ))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #arredonda pra cima
print('a raiz de {} é igual a {}'.format(num, math.floor(raiz)))
from math import sqrt, floor, ceil
num = int(input('Digite um número: ' ))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('a raiz de {} é igual a {}'.format(num, floor(raiz)))

IMPORTAÇÃO DE BIBLIOTECAS
Para conhecer as bibliotecas em Python, podemos acessar o python.org. 
Indo em docs eu posso escolher a versão. Podemos saber a versão que estamos utilizando olhando no canto inferior direito do vs code. 
Vamos clicar em Library reference. E vamos procurar o tópico Numeric and Mathematical Modules, onde temos todas as funcionalidades e exemplos. 
Por exemplo vamos voltar e ver a biblioteca ramdom que é a biblioteca de números aleatórios. Vamos no vs code importar essa biblioteca.
