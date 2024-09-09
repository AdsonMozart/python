numeros = input("Digite numeros inteiros separados por espaço: ").split(" ")
numerosRecebidos = []

for valor in numeros:
    try:
        numero = int(valor)
        if (numero % 2) == 0:
            numerosRecebidos.append(numero)
        else:
            print(f"O número: {numero} não é um valor par, por gentileza tente outro")
    except ValueError:
        print(f"{valor} não é um número inteiro, por gentileza tente outro")

numerosRecebidos.sort(reverse=True)
print("Lista de numeros inteiros em ordem decrescente", numerosRecebidos)