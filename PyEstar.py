import datetime
from time import sleep
import sys


def linha():
    print('=='*20)


now = datetime.datetime.now()
TentativaLogin = 0
saldo = 5
carro_atual = 'você ainda não estacionou um carro'
minuto_atual = now.minute
hora_atual = now.hour
veiculo1 = ''
veiculo2 = ''
veiculo1h = ''
veiculo2h = ''
umcarro = False
doiscarro = False

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
                print(f'Bem Vindo     {now.day}/{now.month}/{now.year}  {hora_atual}:{minuto_atual}')
                print(f'seu saldo atual é de \033[33m{saldo}\033[m Estar que tambem correspondem a {saldo} hrs')
                print('ultímo carro estacionado :', carro_atual)
                print('[1] comprar Estar\n'
                      '[2] definir carro\n'
                      '[3] estacionar\n'
                      '[4] histórico\n'
                      '[5] sair')

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
                    numero_de_carros = int(input('quantos você deseja definir? '))
                    if numero_de_carros == 1:
                        veiculo1 = (str(input("Digite o nome do 1° veículo: ")))
                        print('você cadastrou o veiculo ', veiculo1)
                        umcarro = True
                    elif numero_de_carros == 2:
                        veiculo1 = (str(input("Digite o nome do 1° veículo: ")))
                        veiculo2 = (str(input("Digite o nome do 2° veículo: ")))
                        print('voê cadastrou os veiculos', veiculo1, veiculo2)
                        doiscarro = True
                    linha()
                    continue

                elif opcao == '3':
                    print('seus carros cadastrados são ')
                    if umcarro == True:
                        print(veiculo1)
                    elif doiscarro == True:
                        print(veiculo1, veiculo2)

                    carro_atual = input('digite o nome do carro que você deseja estacionar:  ')

                    if carro_atual == veiculo1:
                        print()
                        TempoEstacionadoH = int(
                            input(f'deseja fica por quanto tempo com seu veículo ({carro_atual})hora(s):\n'
                                  '=> '))
                        if saldo >= TempoEstacionadoH:

                            TempoLimiteH = now.hour + TempoEstacionadoH
                            TempoLimiteM = now.minute
                            print(
                                f'agora são {hora_atual} horas e {minuto_atual}minutos pelo horario de brasília\nvocê poderá ficar '
                                f'estacionado até ás {TempoLimiteH} horas e {TempoLimiteM} minutos')
                            saldo = saldo - TempoEstacionadoH
                            horas1 = TempoLimiteH

                            veiculo1h = (f'o veiculo {veiculo1} ficou estacionado ate as {horas1}h {TempoLimiteM}min')

                            print('*voltando ao menu*')
                            linha()
                            sleep(2)
                        else:
                            print('você não tem saldo suficiente vá até a loja')
                            linha()
                            continue
                    elif carro_atual == veiculo2:
                        print()
                        TempoEstacionadoH = int(input(f'deseja fica por quanto tempo com seu veículo ({carro_atual})hora(s):\n'
                                                      '=> '))
                        if saldo >= TempoEstacionadoH:

                            TempoLimiteH = now.hour + TempoEstacionadoH
                            TempoLimiteM = now.minute
                            print(f'agora são {hora_atual} horas e {minuto_atual}minutos pelo horario de brasília\nvocê poderá ficar'
                                  f'estacionado até ás {TempoLimiteH} horas e {TempoLimiteM} minutos')
                            saldo = saldo - TempoEstacionadoH

                            horas2 = TempoLimiteH

                            veiculo2h = (f'o veiculo {veiculo2} ficou estacionado ate as {horas2}h {TempoLimiteM}min')
                            print('*voltando ao menu*')
                            linha()
                            sleep(2)
                        else:
                            print('você não tem saldo suficiente vá até a loja')
                            linha()
                            continue
                    else:
                        print('você não definiu esse carro!')
                        continue

                elif opcao == '4':
                    print('histórico')
                    print(f'deseja ver o historico de qual carro?\n[1] {veiculo1}\n[2] {veiculo2}')
                    car = input('=> ')
                    if car == '1':
                        print(veiculo1h)
                    if car == '2':
                        print(veiculo2h)

                    linha()

                elif opcao == '5':
                    sys.exit()

        else:
            print('login ou senha invalidos, tente novamente')
            TentativaLogin = TentativaLogin + 1
            linha()
    else:
        print('login ou senha invalidos, tente novamente')
        TentativaLogin = TentativaLogin + 1
        linha()
