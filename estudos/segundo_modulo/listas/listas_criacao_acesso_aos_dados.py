#Declarando lista apenas por colchetes
frutas = ["laranja", "maca", "uva"]

#Declarando lista
frutas = []

letras = list("python")

numeros = list(range(10))
print(list(range(10)))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]

#Criando matriz para exemplificar listas bidimensionais

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
matriz[0][0]
matriz[0][-1]
print(matriz[-1][1], matriz[1][1])

#Exemplificando o fatiamento da lista

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

#Percorrendo a lista com a estrutura de repetição for

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Preenchendo uma lsita baseado na outra de forma convencional

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#Preenchendo uma lista baseado na outra utilizando COMPREENSÃO(forma inline)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Preenchendo uma lista baseado na outra utilizando COMPREENSÃO(forma modificando o valor)

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero ** 2 for numero in numeros]
print(pares)

