
#hacer division en el rango de [-10, 10]


for divisor in range(-10, 10):
    try: 
        resultado = 20 / divisor
    except ZeroDivisionError:
        print(f"No se puede dividir con el divisor {divisor} por que es cero")
    else:
        print(f"operación división 20 {divisor}: {resultado}")
