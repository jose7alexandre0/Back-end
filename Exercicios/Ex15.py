Minha resposta:
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")
RESOLUÇÃO
temperatura = float (input('informe a temperatura em ºC:'))
print('A temperatura de {:.2f}ºC corresponde a {:.2f}of'.format(temperatura, (temperatura*9/5) +32))
