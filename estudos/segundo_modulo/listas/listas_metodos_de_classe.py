# [].append() utilizado para adicionar itens na lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)

#[].clear() utilizado para limpar todos os itens na lista
lista = [1,"Python", [40, 30, 20]]
print(lista)
lista.clear()
print(lista)

#[].copy() cria uma cópia da lista para voc~e alterar o valor sem a original sofrer alteração
lista = [1,"Python", [40, 30, 20]]
l2 = lista.copy()
print(id(l2), id(lista))
l2[0] = 2
print(l2)
print(lista)

#[].count() é utilizado para contar quantas vezes determinado item aparece na sua lista
cores = ["vermelho", "azul", "verde", "azul", "verde", "verde"]

cores.count("vermelho")
cores.count("azul")
cores.count("verde")

#[].extend() é utilizado para mesclar duas listas formando uma só
linguagens = ["python", "js", "c"]
print(linguagens) #["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)#["python", "js", "c", "java", "csharp"]

#[].index() busca a posição do item na lista
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.index("java")) #3
print(linguagens.index("python")) #0

#[].pop() remove um item da lista em forma de pilha, passando o índice do objeto ou não passa nada e ele remove o último
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.pop() #csharp
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python
print(linguagens)

#[].remove() remove um item da lista só que passando o objeto em si
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens) #["python", "js", "java", "csharp"]

#[].reverse() inverte a ordem da lista
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)

#[].sort() ordena a lista de acordo à sua preferência, ordem alfabética, número de letras de forma crescente ou decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
linguagens2 = ["python", "js", "c", "java", "csharp"]
linguagens2.sort(reverse=True)
linguagens3 = ["python", "js", "c", "java", "csharp"]
linguagens3.sort(key=lambda x: len(x))
linguagens4 = ["python", "js", "c", "java", "csharp"]
linguagens4.sort(key=lambda x: len(x), reverse=True)
print(linguagens, linguagens2, linguagens3, linguagens4)

#[].len() verifica o tamanho da lista, quantos elementos tem
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))

#[].sorted() também utilizado para ordenar a lista porém agora é como uma função
linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))



#ADICIONAIS

#[].isinstance() verifica se é true ou false a afirmação
# Verifica se 5 é um inteiro
print(isinstance(5, int))  # Retorna True
# Verifica se "Python" é uma string
print(isinstance("Python", str))  # Retorna True
# Verifica se [1, 2, 3] é uma lista
print(isinstance([1, 2, 3], list))  # Retorna True
# Verifica se (1, 2, 3) é uma tupla
print(isinstance((1, 2, 3), tuple))  # Retorna True





