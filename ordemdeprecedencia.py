# ordem de execução para calculos
# calcula o que esta em parenteses ()
# depois calcula o que esta em potencia **
# depois executa os calculos na seguinte ordem *, /, // e %
# depois ele calcula + e -

#então 5+6 = 11 seguindo a ordem de precedencia.
print(5+3*2)

#então 3*5+16, que depois será 15+16 = 31 seguindo a ordem de precendência.
print(3*5+4**2)

#então 3*9**2 que resultará em 3*81 que será 243 seguindo a ordem de precendência
print(3*(5+4)**2)

#você pode usar calculos com String
print('oi'*5)
print('='*30)

nome='Paula Macedo Santana'
print('Prazer em te conhecer {:30} !'.format(nome))
print('Prazer em te conhecer {:>30} !'.format(nome))
print('Prazer em te conhecer {:^30} !'.format(nome))
print('Prazer em te conhecer {:=^30} !'.format(nome))