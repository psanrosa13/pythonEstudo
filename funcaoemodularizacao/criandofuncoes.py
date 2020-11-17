def preencheInventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: '),
                       float(input('Valor: ')),
                       int(input('Número Serial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resposta = input('Digite \'S\' para continuar: ').upper()


def exibirInvetario(lista):

    for elemento in lista:
        print('Nome..........: ', elemento[0])
        print('Valor.........: ', elemento[1])
        print('Serial........: ', elemento[2])
        print('Departamento..: ', elemento[3])


def localizarPorNome(lista):

    busca = input('/nDigite o nome do equipamento que deseja buscar: ')

    for elemento in lista:
        if busca == elemento[0]:
            print('Valor.........: ', elemento[1])
            print('Serial........: ', elemento[2])

