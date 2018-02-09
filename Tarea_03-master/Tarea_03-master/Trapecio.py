#Autor: Felipe Gomez Portugal
#Programam que
import math



a = int(input("Escribe la longitud de la base mayor: "))
b = int(input("Escribe la longitud de la base menor: "))
c = int(input("Escribe la altura: "))

formula = int((a + (a+2*c))*b)/2

print ("area: " ,formula)

bit = a+b
root = (bit**2) * (c**2)
lol = math.sqrt(root)
peri= a+b+lol

print (lol)