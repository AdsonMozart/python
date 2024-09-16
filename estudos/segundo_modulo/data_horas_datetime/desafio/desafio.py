from datetime import datetime
import pytz

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Qual operação deseja realizar? => """

saldo = 0
limite = 500
extrato = ""
numero_transacao = 0
LIMITE_TRANSACAO = 10
registros = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            #Adicionando o valor do depósito ao saldo
            saldo += valor
            # Adicionando o horário do saque
            hora_deposito = datetime.now(pytz.timezone("America/Sao_Paulo"))
            registro_deposito_formatado = (hora_deposito.strftime("%d/%m/%y %H:%M:%S"))
            #Adicionando o depósito ao extrato
            extrato += f"Deposito realizado no valor de: {valor:.2f} na seguinte data e horário: {registro_deposito_formatado}\n"
            numero_transacao += 1
        else:
            print("Valor inválido, por gentileza tente novamente!")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        excede_saldo = valor > saldo
        excede_limite =  valor > limite
        excede_transacoes = numero_transacao >= LIMITE_TRANSACAO

        if excede_limite:
            print("O valor excedeu o limite diário!")
        elif excede_transacoes:
            print("Você excedeu o limite de transações diárias!")
        elif excede_saldo:
            print("Você não tem saldo suficiente para sacar tal valor!")
        elif valor > 0:
            saldo -= valor
            # Adicionando o horário do saque
            hora_saque = datetime.now(pytz.timezone("America/Sao_Paulo"))
            registro_saque_formatado = (hora_saque.strftime("%d/%m/%y %H:%M:%S"))
            extrato += f"Saque realizado no valor de: {valor:.2f} na seguinte data e horário: {registro_saque_formatado}\n"
            numero_transacao += 1
        else:
            print("Valor inválido, por gentileza tente novamente!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida!")