'''
Escribe un programa que muestre los números perfectos entre 1 y 1000. 
Definición: Los números perfectos son aquellos cuya suma de sus divisores propios es igual al número. 
Definición: Los divisores propios de un número son aquellos que dividen a un número en forma exacta, residuo igual a cero.
Ejemplo de número perfecto: numero = 6. Divisores propios 1, 2, 3. Suma de divisores propios = 6. 6 = 6.
'''


def calcular_divisores(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(num):
    suma_divisores = sum(calcular_divisores(num))
    return suma_divisores == num

def encontrar_numeros_perfectos(inicio, fin):
    numeros_perfectos = []
    for num in range(inicio, fin+1):
        if es_numero_perfecto(num):
            numeros_perfectos.append(num)
    return numeros_perfectos

inicio = 1
fin = 1000
numeros_perfectos = encontrar_numeros_perfectos(inicio, fin)
print("Números perfectos entre", inicio, "y", fin, ":", numeros_perfectos)

    
