#Escribe un programa para calcular el cociente de dos números enteros en forma recursiva e iterativa. Hint:
#Reduce uno de los números restándole el otro número hasta llegar a cero o que no se pueda dividir.
def division_recursiva(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + division_recursiva(dividendo - divisor, divisor)

def division_iterativa(dividendo, divisor):
    contador = 0
    while dividendo >= divisor:
        dividendo -= divisor
        contador += 1
    return contador

num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))

print("Cociente por recursión: ", division_recursiva(num1, num2))
print("Cociente por iteración: ", division_iterativa(num1, num2))   