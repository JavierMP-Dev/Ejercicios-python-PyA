#Escribe un programa que lea un número entero de 3 cifras y muestre por separado las cifras de ese número.
#Hacer esto aplicando los operadores %, / y // únicamente. No convertirlo a «string»
num = int(input("Ingrese un numero de 3 dígitos: "))

#tranformado numero mediante operaciones 

centenas = num // 100
decenas = (num % 100) // 10
unidades = num % 10

print ("Centenas ", centenas)
print ("decenas  ", decenas )
print ("unidades", unidades)