#programa para obtener los numeros de fibonacci
#el progrma se encunetra dentro de un ciclo while para hacer varias pruebas sin tener que ejecutarlo en cada una de ellas
print ("Imprimiendo la serie fibonacci")
compa = 0
while compa ==1:

    limite = int(input("Ingrese el numero que quiera concer de la serie: "))

    def fibo (lim):
        if lim <= 0:
            return 0
        elif lim == 1:
            return 1

        return fibo(lim-1)+fibo(lim-2)

    for i in range (limite):
        print(fibo(i))
respuesta = int(input("\nDesea repetir presione 1"))
respuesta = compa