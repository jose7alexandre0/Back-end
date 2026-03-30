BIBLIOTECA RANDOM (3 TEC)
import random
num = random.random()#computador vai gerar um número aleatório, entre 0 e um
num2 = random.randint(1,10)
print(num)
print(num2)

IMPORTAÇÃO DE BIBLIOTECAS
Se digitar o comando import e ctrl+espaço conseguimos ver todas as bibliotecas disponíveis para usar no python.
Vamos voltar para a página inicial do python.org e vamos no pypi. O py vem de python e o pi e de package index que 
significa de pacotes extras, que são funcionalidades foras do python que podem ser utilizadas no python. Programadores da
comunidade podem publicar pacotes para outras pessoas utilizarem. Por exemplo eu posso fazer um módulo para verificar cpf.

IMPORTAÇÃO DE BIBLIOTECAS
Por exemplo vamos procurar por emoji para mostrar emoji. Se fizermos import emoji no vs code não vai aparecer para a gente completar 
isso porque não temos ela baixada. Para isso vamos no terminal e instalamos a biblioteca pelo pip install emoji, se der certo já deve aparecer 
no vs code a biblioteca emoji como opção. Vamos voltar no site e ver qual emojis podemos utilizar no emoji sheet e copiar o emoji que a gente quer.
Vamos voltar no vscode e colar o seguinte código.

IMPORTAÇÃO DE BIBLIOTECAS
import emoji
print(emoji.emojize("Olá, mundo "))
