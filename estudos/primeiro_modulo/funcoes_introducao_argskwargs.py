def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Bokita"):
    print(f"Seja bem-vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Adson")
exibir_mensagem_3()
exibir_mensagem_3(nome="Guxtântrico")


#Retornando mais de um valor
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34])) #64
print(retorna_antecessor_e_sucessor(10)) #(9, 11)
print(func_3())


#Salvar carro no banco de dados (*args e **kwargs)
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio",1999, "ABC-1234") #Desvantagem de obrigatoriamente manter a ordem, uma vez que não é no modelo chave e valor
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})