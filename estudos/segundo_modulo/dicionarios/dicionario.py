#A forma como o dicionário pode ser visto
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

#A segunda forma que o dicionário pode ser visto
pessoa_2 = dict(nome="Guilherme", idade =28)
print(pessoa_2)

#Se por acaso já tiver algum dicionário e você quiser apenas adicionar uma chave e um valor
pessoa["telefone"] = "3333-1234"
print(pessoa)

#Caso queira acessar alguma chave do container
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])


#Como acessar chaves e valores de dicionários aninhados
contatos = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224", "extra": {"a": 1}},
}

telefone = contatos["gustavo@gmail.com"]["telefone"]
print(telefone)

extra = contatos["adson@gmail.com"]["extra"]["a"]
print(extra)


#Iteração dos elementos do dicionário
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)