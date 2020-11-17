with open('iris.data','r') as arquivo:
    basedados = []
    for registro in arquivo.readlines():
        basedados.append(registro.split(','))

print(basedados)

print(basedados[0][0])