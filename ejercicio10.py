
#hacer division en el rango de [-10, 10]


for divisor in range(-10, 10): #recorriendo mediante ciclo for
    try: #haciendo operacion en cada iteracion
        resultado = 20 / divisor 
    except ZeroDivisionError:#manejo del error si intento dividir entre cero
        print(f"No se puede dividir con el divisor {divisor} por que es cero")
    else:   #si no hay error salto a esta parte y continua la ejecucion
        print(f"operación división 20 {divisor}: {resultado}")
