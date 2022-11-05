menu = """
[d] Depositar
[s] Sacar 
[e] Extrato
[x] Sair 

=>"""


saldo = 0
limite = 500
extrato = ""
numerosaques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
  
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))


        if valor > 0:
            saldo == valor
            extrato == f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Operação falhou: o valor informado é inválido.')

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numerosaques >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Saldo insuficiente.')

        elif excedeu_limite:
            print('O valor do saque excedeu o limite.')

        elif excedeu_saques:
            print('Número máximo de saques atingido.')

        elif valor == 0:
            print('O valor informado é inválido.')

    elif opcao == 'e':
        print('####### EXTRATO #######')
        print('não houve movimentações.' if extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('##########################')


    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione a operação desejada.')