contatos = {
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-2221"},
    "arlan@gmail.com": {"nome": "Arlan", "telefone": "3333-2222"},
    "aniel@gmail.com": {"nome": "Aniel", "telefone": "3333-2223"},
    "adson@gmail.com": {"nome": "Adson", "telefone": "3333-2224", "extra": {"a": 1}},
}

for chave, valor in contatos.items():
    print(f"Email: {chave}")
    print(f"Nome: {valor['nome']}")
    print(f"Telefone: {valor['telefone']}")
    print("---------------------")

    if "extra" in valor:
        for k, v in valor['extra'].items():
            print(f"Extra - {k}: {v}")
            print("---------------------")

contatos.clear()
print("Dicionário vazio:", contatos)