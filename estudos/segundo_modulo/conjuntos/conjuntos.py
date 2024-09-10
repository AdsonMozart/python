print(set([1, 2, 3, 1, 3, 4])) # {1, 2, 3, 4}
print(set("abacaxi")) # {"b", "a", "c", "x", "i"}
print(set(("palio", "gol", "celta", "palio"))) # {"gol", "celta", "palio"}

#Para percorrer entre os índices de um conjunto, primeiro tem que transformar em lista
numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros[0])


# {}.union é utilizado para unir dois conjuntos diferentes
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))


# {}.intersection é utilizado para unir os elementos iguais de dois conjuntos diferentes
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

print(conjunto_c.intersection(conjunto_d))


# {}.difference é utilizado para mostrar o que há de diferente em um conjunto quando comparado a outro diferente de forma separada
conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}

print(conjunto_e.difference(conjunto_f))
print(conjunto_f.difference(conjunto_e))


# {}.symmetric_difference é utilizado para mostrar o que há de diferente em um conjunto quando comparado a outro diferente de forma única
conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}

print(conjunto_g.symmetric_difference(conjunto_h))


# {}.issubset retorna em booleano se um conjunto é pertecente a outro ou não
conjunto_i = {1, 2, 3}
conjunto_j = {4, 1, 2, 5, 6, 3}

print(conjunto_i.issubset(conjunto_j))


# {}.isdisjoint retorna em booleano se um conjunto tem todos os elementos diferentes de um outro conjunto
conjunto_k = {1, 2, 3, 4, 5}
conjunto_l = {6, 7, 8, 9}
conjunto_m = {1, 0}

print(conjunto_k.isdisjoint(conjunto_l))
print(conjunto_k.isdisjoint(conjunto_m))


# {}.add adiciona um elemento, se ele não já pertencer ao grupo
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)


# {}.copy cria uma cópia do seu conjunto
sorteio_b = {1, 23}
sorteio_b
sorteio.copy()

print(sorteio_b)


# {}.discard descarta um valor da sua lista, uma vez que a unificação de números repetidos é automática
numeros_b = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros_b)
numeros_b.discard(1)
print(numeros_b)


# {}.pop vai removendo em ordem de índice os elementos do conjunto
numeros_c = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros_c)
numeros_c.pop()
numeros_c.pop()
print(numeros_c)


# {}.remove um elemento de sua lista, a diferença para o discard é que se o elemento não existir ele dá erro
numeros_d = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros_d)
numeros_d.remove(2)
print(numeros_d)

# len faz a contagem de elementos

#in verifica se tem o número informado dentro do conjunto


