#Escribe un programa lea en una variable con una velocidad en Km/h y la transforme a m/s.
#Autor: Javier Montoya

veloci = int(input("Ingresa la velocidad en km/h: "))

metro = (veloci * 1000) / 3600

print ("La velocidad resultande es:", metro, "m/s")