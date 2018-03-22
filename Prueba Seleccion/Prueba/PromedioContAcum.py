def main():
    numAprobadas = 0
    sumaAprobadas = 0

    for k in range(5):
        calificacion = int(input("Calificación: "+ str(k+1)))
        if calificacion>=70:
            numAprobadas = numAprobadas + 1
            sumaAprobadas += calificacion

    if numAprobadas>0:
         promedio = sumaAprobadas/numAprobadas
         print("Promedio: %.1f"% promedio)
    else:
        print("No hay promedio")

main()