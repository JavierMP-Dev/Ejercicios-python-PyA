
#algoritmo para obtener factoriales

num = int(input("Ingrese un numero: "))


def factorial (base):
        if base == 0:
            return 1
        return base * factorial(base - 1)

print (factorial(num))