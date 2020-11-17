nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
if idade >= 65:
    print('O paciente {} POSSUI atendimento prioritário!'.format(nome))
else:
    print('O paciente {} NÃO POSSUI atendimento prioritário!'.format(nome))