#Autor: Felipe Gomez Portugal Trueba
#Calcular la hora actual, dado los segundos desde la media noche.

segundos = int(input("Teclea los segundos: "))

h = segundos//3600
m = (segundos%3600) //60
s = (segundos%3600) %60

print ("La hora es: %i:%02i:%i" % (h,m,s))