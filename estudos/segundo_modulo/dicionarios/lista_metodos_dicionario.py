#{}.clear vai lempar as chaves e atribuições do dicionário
contatos = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224", "extra": {"a": 1}},
}
print(contatos)
contatos.clear()
print(contatos)


#{}.copy você cria uma cópia do seu dicionário
contatos_2 = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"}
}
copia = 4*5000

print(copia)