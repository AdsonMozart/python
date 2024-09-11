#{}.clear vai limpar as chaves e atribuições do dicionário
contatos = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224", "extra": {"a": 1}},
}
print(contatos)
contatos.clear()
print(contatos)
print("---------------")


#{}.copy você cria uma cópia do seu dicionário
contatos_2 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
copia = contatos.copy()
copia["gustavo@gmail.com"] = {"nome": "GuxTântrico"}
print(contatos_2["gustavo@gmail.com"])
print(copia["gustavo@gmail.com"])
print("---------------")


#{}.fromkeys da primeira forma você atribui valor vazio às chaves, da segunda forma você cria todas as chaves e atribui aquele valor
dict.fromkeys(["nome", "telefone"]) #{"nome": None, "telefone": None}
(dict.fromkeys(["nome", "telefone"], "vazio")) #{"nome": "vazio", "telefone": "vazio"}


#{}.get uma segunda forma de acessar valores dentro do dicionário
contatos_3 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
# print(contatos_3["chave"]) #KeyError
contatos_3.get("chave") #None
print(contatos_3.get("chave", {}))
print(contatos_3.get("gustavo@gmail.com",{}))
print("---------------")


#{}.items retorna os itens do dicionário em formas de tuplas, super importante quando se precisa iterar pelo comando for
contatos_4 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
print(contatos_4.items())
print("---------------")


#{}.keys esse metodo retorna somente as chaves do dicionário
contatos_4 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
print(contatos_4.keys())
print("---------------")


#{}.pop irá remover um valor do seu dicionário quando informado uma chave
contatos_4 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
print(contatos_4.pop("gustavo@gmail.com"))
print(contatos_4.pop("gustavo@gmail.com", "Não encontrou"))
print("---------------")


#{}.pop irá remover um valor do seu dicionário conforme a ordem de sequência
contatos_5 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
print(contatos_5.popitem())
#print(contatos_5.popitem() KeyError
print("--------------- - ------")


#{}.setdefault se eu selecionar uma chave já existente pra atribuir um valor ele não deixa e retorna o valor predominante, se a chave não existir ele adiciona a chave e o valor passado
contatos_6 = {"nome": "Gustavo", "telefone": "3333-2221"}
print(contatos_6.setdefault("nome", "Nenel"))
print(contatos_6.setdefault("idade", 24))
print(contatos_6)


#{}.update permite que atualizemos o dicionário
contatos_7 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
contatos_7.update({"gustavo@gmail.com": {"nome": "Adseixons"}})
print(contatos_7)
contatos_7.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "4321-1234"}})
print(contatos_7)
print("___________________")


#{}.values metodo que retorna somente os valores
contatos_8 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224"},
}
print(contatos_8.values())
print("-_-_-_-_-_-_-_-_-_-_-")


# in você verifica se tem essa chave no dicionário, retornando a resposta em booleano
contatos_9 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224"},
}
resultado = "gustavo@gmail.com" in contatos_9
print(resultado)
print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´")



# del você pode remover o atributo de uma chave ou uma chave completa
contatos_10 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224"},
}
del contatos_10["gustavo@gmail.com"]["telefone"]
print(contatos_10)
del contatos_10["aniel@gmail.com"]
print(contatos_10)
del contatos_10
print(contatos_10)


