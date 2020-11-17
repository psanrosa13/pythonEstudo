import math

numero = int(input('Digite um numero: '))

raizquadrada = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, raizquadrada))
print('A raiz de {} é igual a arrendodado para cima {}'.format(numero, math.ceil(raizquadrada)))
print('A raiz de {} é igual a arrendodado para baixo {}'.format(numero, math.floor(raizquadrada)))
