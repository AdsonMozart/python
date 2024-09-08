curso = "pYtHon"

print(curso.upper()) #Tudo em maiúsculo
print(curso.lower()) #Tudo em minúsculo
print(curso.title()) #Apenas a primeira letra maiúscula

print(curso.strip()) #Para remover os espaços à direita e à esquerda
print(curso.lstrip()) #Para remover os espaços à esquerda
print(curso.rstrip()) #Para remover os espaços à direita

print(curso.center(10, "x").lower()) #Para preencher os espaços da string, de acordo com o parâmetro informado
print(";".join(curso).title()) #Para preencher entre os caracteres da string informada, de acordo com o parâmetro informado
