from datetime import date, datetime, timedelta

tipo_carro = """

Press [P] if your car is a SMALL SIZE 
Press [M] if your car is a MEDIUM SIZE
Press [G] if your car is a BIG SIZE
Press [S] to exit

What operation do you want to perform? =>
"""


tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

sair = True

while sair:

    tipo_carro_selecionado= input(tipo_carro)

    if tipo_carro_selecionado == "P":
        estimativa_entrega = data_atual + timedelta(minutes=tempo_pequeno)
        print(f"O carro chegou: {data_atual}, e será entregue: {estimativa_entrega}")
    elif tipo_carro_selecionado == "M":
        estimativa_entrega = data_atual + timedelta(minutes=tempo_medio)
        print(f"O carro chegou: {data_atual}, e será entregue: {estimativa_entrega}")
    elif tipo_carro_selecionado == "G":
        estimativa_entrega = data_atual + timedelta(minutes=tempo_grande)
        print(f"O carro chegou: {data_atual}, e será entregue: {estimativa_entrega}")
    elif tipo_carro_selecionado == "S":
        sair = False
    else:
        print("Opção inválida, por favor informe um valor válido!")

#Para realizar o decréscimo de dias basta importar e realizar a operação
print(date.today() - timedelta(days=1))