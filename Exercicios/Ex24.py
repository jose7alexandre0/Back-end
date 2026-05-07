cidade = str(input('Em que cidade você nasceu? ')).strip()
comeca_com_santo = cidade[:5].upper() == 'SANTO'
print(f'A cidade começa com a palavra "Santo"? {comeca_com_santo}')

RESOLUÇÃO
cidade = str(input('Em que cidade você nasceu?')).strip()
n1 = cidade.lower()
print('santo' in n1)
