#Autor: Felipe Gomez Portugal
#Calcula la calificaicon final, dado el resultado de 4 exámenes

Examen1 = int(input("Calificación de examen 1: "))
Examen2 = int(input("Calificación de examen 2: "))
Examen3 = int(input("Calificación de examen 3: "))
Examen4 = int(input("Calificación de examen 4: "))
Promedio = int((Examen1*0.4)+(Examen2*0.2)+(Examen3*0.1)+(Examen4*0.3))
print ("Tu promedio es: ",Promedio)