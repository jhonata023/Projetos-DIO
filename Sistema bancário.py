saldo = 0
cont = 0
print('Bem vindo ao nosso sistema bancário.')
while True:
    print('=-' * 6, 'MENÚ', '=-' * 6)
    print('''    [ 1 ] SAQUE
    [ 2 ] EXTRATO
    [ 3 ] DEPÓSITO
    [ 0 ] SAIR''')
    print('=-' * 15)

    opção = int(input('Digite sua operação: '))

    if opção == 1:
        while True:
            saque = int(input(f'''Seu saldo é de R${saldo:.2f}.
Digite o valor a ser sacado: R$'''))
            if cont > 2:
                print('Seu limite de saque foi esgotado.')
                break
            elif saque > saldo:
                print('Saldo insuficiente. Por favor, tente novamente.')
            elif saque > 500:
                print('Seu limite de saque é de R$500,00. Por favor, tente novamente.')
            else:
                saldo -= saque
                print(f'Seu agora é R${saldo:.2f}')
                cont += 1
                break
    if opção == 2:
        print(f'Seu saldo é de R${saldo:.2f}')
    elif opção == 3:
        while True:
            depósito = int(input('Digite o valor a ser depositado: R$'))
            if depósito <= 0:
                print('Opção inválida. Por favor, insira um valor positivo.')
            elif depósito > 0:
                saldo += depósito
                break
    elif opção == 0:
        print('Obrigado por utilizar nosso sistema. Volte logo!')
        break
    elif opção > 3:
        print('Opção inválida, por favor tente novamente.')
    elif opção < 0:
        print('Opção inválida, por favor tente novamente.')
