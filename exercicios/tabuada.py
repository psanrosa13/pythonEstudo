numero = int(input('Digite um numero para calcular a tabuada: '))
contador = 1

while contador <= 10:
    print('{} x {} = {}'.format(numero, contador, numero * contador))
    contador = contador + 1
