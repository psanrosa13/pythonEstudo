from math import ceil
from math import floor
from math import sqrt

numero = int(input('Digite um numero: '))

raizquadrada = sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, raizquadrada))
print('A raiz de {} é igual a arrendodado para cima {}'.format(numero, ceil(raizquadrada)))
print('A raiz de {} é igual a arrendodado para baixo {}'.format(numero, floor(raizquadrada)))
