inventario = []
resposta = 'S'

while resposta=='S':
    equipamento = [input('Equipamento: '),
                float(input('Valor: ')),
                int(input('Número Serial: ')),
                input('Departamento: ')]
    inventario.append(equipamento)
    resposta=input('Digite \'S\' para continuar: ').upper()

for elemento in inventario:
    print('Nome..........: ',elemento[0])
    print('Valor.........: ', elemento[1])
    print('Serial........: ', elemento[2])
    print('Departamento..: ', elemento[3])

busca = input('/nDigite o nome do equipamento que deseja buscar: ')

for elemento in inventario:
    if busca == elemento[0]:
        print('Valor.........: ', elemento[1])
        print('Serial........: ', elemento[2])