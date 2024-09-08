#Exibir o resultado de oerações por função
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao_anterior):
    resultado = funcao_anterior(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

#Utilização do escolpo global

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) #2500
print(salario_com_bonus)
print



