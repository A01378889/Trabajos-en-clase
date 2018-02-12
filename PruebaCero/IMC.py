#Autor: Felipe Gomez Portugal Trueba
#Calcular el IMC; dado el peso y estatura

peso = int(input("Cual es tu peso: "))
estatura = float(input("Cual es tu estatura: "))

imc = peso / estatura**2

print ("Este es tu IMC: %.2f " %imc)