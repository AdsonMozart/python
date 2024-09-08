#Metodo porcentagem (desuso)

nome = "Gaulis Tantrico"
idade = 24
profissao = "Massagista tântrico"
linguagem = "viadagem"

dados = {"nome": "Gaulis Tantrico", "idade": 24, "profissao": "Massagista tântrico", "linguagem": "viadagem4"}

print("Olá, eu sou o %s. Tenho %d anos de idade, trampo como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

#Metodo format

nome = "Gaulis Tantrico"
idade = 24
profissao = "Massagista tântrico"
linguagem = "viadagem"

print("Olá, eu sou o {}. Tenho {} anos de idade, trampo como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))#Modo 1
print("Olá, eu sou o {3}. Tenho {0} anos de idade, trampo como {1} e estou matriculado no curso de {2}." .format(nome, idade, profissao, linguagem))#Modo 2
print("Olá, eu sou o {nome}. Tenho {idade} anos de idade, trampo como {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))#Modo 3
print("Olá, eu sou o {nome}. Tenho {idade} anos de idade, trampo como {profissao} e estou matriculado no curso de {linguagem}." .format(**dados))#Modo 4 (Funciona com dicionário)

#Metodo f-string (mais utilizado)

nome = "Gaulis Tantrico"
idade = 24
profissao = "Massagista tântrico"
linguagem = "viadagem"

print(f"Olá, eu sou o {nome}. Tenho {idade} anos de idade, trampo como {profissao} e estou matriculado no curso de {linguagem}.")#Modo 1

#Formatando strings com f-string

PI= 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:8.2f}")



