saldo = 0.0 
transacoes = []

while True:
    print("\n=== CAIXA ELETRONICO ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    #validação da opção usando while
    while opcao not in ["1", "2", "3", "4"]: 
        print("Opção invalida, Tente novamente. ")
        opcao = input("Escolha  uma opção")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        #validação do valor  usando while 
        while valor <= 0:
            print("0 valor deve ser positivo.")
            valor = float(input("Digite o valor do depósito "))

        saldo += valor
        transacoes.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")


    elif opcao == "2":
        valor = float(input("Digite o valor do saque:"))
        
        #validação do valor usando while 
        while valor <= 0:
            print("O valor deve ser positivo.")
            valor = float(input("Digite o valor do saque: "))

        if valor <= saldo:
            saldo -= valor
            transacoes.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    elif opcao == "3":
        print("\n=== EXTRATO ===")
        if len(transacoes) == 0:
            print("Nenhuma transação realizada.")
        else:
            for t in transacoes:
                print(t)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Encerrando o programa...")
        break
            