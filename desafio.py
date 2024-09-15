menu = """
╔═════════════════════════════╗
║        B I T   &   $        ║
║      [ Banco Digital ]      ║
╠═════════════════════════════╣
║ [d] Depositar               ║
║ [s] Sacar                   ║
║ [e] Extrato                 ║
║ [l] Consultar Limite        ║
║ [r] Redefinir Conta         ║
║ [q] Sair                    ║
╚═════════════════════════════╝
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n===== EXTRATO =====")
        print("Nenhuma movimentação" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================")

    elif opcao == "l":
        print(f"\nSeu limite atual é de: R$ {limite:.2f}")
        print(f"Você pode realizar {LIMITE_SAQUES - numero_saque} saques restantes hoje.")

    elif opcao == "r":
        confirmar = input("Você tem certeza que deseja redefinir o saldo e o extrato? [s/n]: ")
        if confirmar == "s":
            saldo = 0
            extrato = ""
            numero_saque = 0
            print("Conta redefinida com sucesso!")
        else:
            print("Operação de redefinição cancelada.")

    elif opcao == "q":
        print("Saindo... Obrigado por utilizar o B I T & $.")
        break

    else:
        print("Operação inválida! Selecione uma opção válida e tente novamente.")