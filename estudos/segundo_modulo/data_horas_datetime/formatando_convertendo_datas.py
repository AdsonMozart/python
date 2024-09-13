import datetime

d = datetime.datetime.now()

#Formatando data e hora
print(d.strftime("%d/%m/%y %H:%M:%S"))

#Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)