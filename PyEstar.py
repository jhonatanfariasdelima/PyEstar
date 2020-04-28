import datetime
from time import sleep
import sys


def linha():
    print('=='*20)


now = datetime.datetime.now()
TentativaLogin = 0
saldo = 2
carro_atual = 'você ainda não estacionou um carro'
total_carros = []
linha()
print('\033[31m Estar curitiba\033[m')
print('')
while TentativaLogin < 3:
    login = input('Digite seu login: ')
    senha = input('Dgite sua senha: ')
    linha()
    if login == 'jhoni':
        if senha == '33':

            while True:
                print(f'Bem Vindo     {now.day}/{now.month}/{now.year}  {now.hour}:{now.minute}')
                print(f'seu saldo atual é de \033[33m{saldo}\033[m Estar que tambem correspondem a {saldo} hrs')
                print('ultímo carro estacionado :', carro_atual)
                print('[1] comprar Estar\n'
                      '[2] definir carro\n'
                      '[3] estacionar\n'
                      '[4] sair')

                linha()
                opcao = input('o que você deseja fazer agora? ')
                linha()

                if opcao == '1':
                    linha()
                    print('\033[31mBem Vindo a Nossa LOJA\033[m')
                    quant_compra = int(input('valor unitário = R$ 3\nquantos Estar você deseja comprar? '))
                    saldo = saldo + quant_compra
                    print(f'valor total a pagar = R$ {quant_compra * 3}')
                    print('retornando...')
                    linha()
                    sleep(2)
                    continue

                elif opcao == '2':
                    print('vamos definir seu carro agora!')
                    total_de_carros = int(input('quantos você deseja definir? '))
                    for carro in range(total_de_carros):
                        total_carros.append(str(input("Digite o nome do veículo: ")))
                    print('voê cadastrou os veiculos',total_carros)
                    linha()
                    continue

                elif opcao == '3':
                    print('seus carros cadastrados são ',total_carros)
                    carro_atual = input('digite o nome do carro que você deseja estacionar:  ')
                    if carro_atual in total_carros:

                        print()
                        TempoEstacionadoH = int(input(f'deseja fica por quanto tempo com seu veículo ({carro_atual}) hora(s):\n'
                                                      '=> '))
                        if saldo >= TempoEstacionadoH:
                            TempoLimiteH = now.hour + TempoEstacionadoH

                            print(f'agora são {now.hour} horas e {now.minute} minutos pelo horario de brasília\nvocê poderá ficar '
                                  f'estacionado até ás {TempoLimiteH} horas e {now.minute} minutos')
                            saldo = saldo - TempoEstacionadoH
                            print('*voltando ao menu*')
                            linha()
                            sleep(2)

                        else:
                            print('você não tem saldo suficiente vá até a loja')
                            continue

                elif opcao == 4:
                    sys.exit()

        else:
            print('login ou senha invalidos, tente novamente')
            TentativaLogin = TentativaLogin + 1
            linha()
    else:
        print('login ou senha invalidos, tente novamente')
        TentativaLogin = TentativaLogin + 1
        linha()

