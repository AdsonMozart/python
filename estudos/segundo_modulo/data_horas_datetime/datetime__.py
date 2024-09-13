from datetime import date, datetime, time

#Utilizando a classe date você consegue armazenar a data no padrão solicitado
data = date(2024, 9, 13)
print(data)

#Com o metodo today para date você armazena e imprime a data do dia
print(date.today())

#Utilizando a classe datetime você consegue armazenar a data e a hora no padrão solicitado
data_hora = datetime(2024, 9, 13)
print(data_hora)

#Com o metodo today para date você armazena e imprime a data e o horário do dia
print(datetime.today())

#Utilizando a classe time você consegue armazenar a hora no padrão solicitado
hora = time(10, 20, 0)
print(hora)

#------------------------------------------------------
#------------EXERCÍCIO---------------------------------
#------------------------------------------------------
print("----------------------------------------------")


import datetime

#Criando data e hora
d = datetime.datetime(2024, 7, 19, 13, 45)
print(d)

#Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)