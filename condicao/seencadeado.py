nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa?').upper()
if idade >= 65:
    print('O paciente {} POSSUI atendimento prioritário!'.format(nome))
elif doenca_infectocontagiosa=='SIM':
    print('O paciente {} deve ser direcionada para sala de espera reservada!'.format(nome))
else:
    print('O paciente {} NÃO POSSUI atendimento prioritário!'.format(nome))