import datetime
from time import sleep

now = datetime.datetime.now()

def linha():
    print('=='*20)


saldo = 2
carro_atual = 'defina um ou dois carros'
linha()
print('\033[31m Estar curitiba\033[m')
print('')
while True:
    login = input('Digite seu login: ')
    senha = input('Dgite sua senha: ')
    linha()
    if login == 'jhoni':
        if senha == '33':

            while True:
                print(f'Bem Vindo     {now.day}/{now.month}/{now.year}  {now.hour}:{now.minute}')
                print(f'seu saldo atual é de \033[33m{saldo}\033[m Estar que tambem correspondem a {saldo} hrs')
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
                    linha()
                    continue

                elif opcao == '2':
                    print('')

                elif opcao == '3':
                    print(f'deseja fica por quanto tempo com seu veículo ({carro_atual}) ?')

                    TempoEstacionadoH = int(input('hora(s): '))

                    if saldo >= TempoEstacionadoH:
                        TempoLimiteH = now.hour + TempoEstacionadoH

                        print(f'agora são {now.hour} horas e {now.minute} minutos pelo horario de brasília\nvocê poderá fica '
                              f'estacionado até ás {TempoLimiteH} horas e {now.minute}')
                        print('voutando ao menu')
                        linha()
                        sleep(2)

                        saldo = saldo - TempoEstacionadoH
                    else:
                        print('você não tem saldo suficiente vá até a loja')
                        continue
                elif opcao == 4:
                    print('')
        else:
            print('login ou senha invalidos, tente novamente')
            linha()
    else:
        print('login ou senha invalidos, tente novamente')
        linha()

