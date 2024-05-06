#funcion para leer nombres 
#El primer dato para leer es el nombre, puede ser que tenga más de uno; En ese caso se toma el primer nombre, 
#siempre y cuando este primer nombre no sea "Maria" o "José".
def leer_nombres():
    """Lee los nombres"""
    print('¿Cuáles son tus nombres? (Mayúsculas y sin acentos)')
    nombres = input('>>>').strip().split()
    
    # Verificar si se proporcionaron nombres y tomar el primero
    if nombres:
        primer_nombre = nombres[0].upper()
        
        # Verificar si el primer nombre es "MARIA" o "JOSE"
        if primer_nombre in ["MARIA", "JOSE"]:
            # Tomar el segundo nombre si existiera
            if len(nombres) > 1:
                return nombres[1].upper()
            else:
                return ""
        else:
            return primer_nombre
    else:
        return ""


#funcion solicitar apellidos 
#Leer los apellidos no representa ningún problema, solamente los convertimos a mayúsculas.
def leer_apellidos():
    """Lee los apellidos"""
    print('¿Cuáles son tus apellidos? (Mayúsculas y sin acentos)')
    primer_apellido = input('Primer apellido: ').upper()
    segundo_apellido = input('Segundo apellido: ').upper()
    return primer_apellido, segundo_apellido


#Fecha de nacimiento
#Cómo se mencionó arriba, es necesario validar que el año de nacimiento sea correcto.
def leer_anio_nacimiento():
    """Lee el año de nacimiento"""
    print('¿En qué año naciste? (4 dígitos)')
    anio_nacimiento = input('>>>')
    while not anio_nacimiento.isnumeric() or len(anio_nacimiento) != 4:
        anio_nacimiento = input('>>>')
    return anio_nacimiento

#mes de nacimiento
#En el caso de los meses, tal vez no quisiéramos pedirle el mes de nacimiento como 
#dos caracteres si no dar al usuario y la opción de elegir su mes de nacimiento a través de un menú.
def leer_mes_nacimiento():
    """Lee el mes de nacimiento"""
    print('¿En qué mes naciste? (2 dígitos)')
    mes_nacimiento = input('>>>')
    while not mes_nacimiento.isnumeric() or len(mes_nacimiento) != 2:
        mes_nacimiento = input('>>>')
    return mes_nacimiento

#dia de nacimiento
#En el caso del día, debemos validar que sea un número entero positivo, mayor que cero y menor que 32 en unos casos, menor que 31 en otros
#casos y menor que 30 o 29 en el caso del mes de febrero.
def leer_dia_nacimiento():
    """Lee el día de nacimiento"""
    print('¿En qué día naciste? (2 dígitos)')
    dia_nacimiento = input('>>>')
    while not dia_nacimiento.isnumeric() or len(dia_nacimiento) != 2:
        dia_nacimiento = input('>>>')
    return dia_nacimiento

#Leer exceso no representa ningún problema, aunque es posible no proporcionar p
#un valor por cuestiones de diversidad. En tal caso, hay que regresar una "X".
def leer_sexo():
    """Lee el sexo"""
    print('¿Cuál es tu sexo? (H/M)')
    sexo = input('>>>').upper()
    while sexo not in ['H', 'M']:
        sexo = input('>>>').upper()
    return sexo


#entidad
entidades = {'AG':'Aguascalientes',
             'BC':'Baja California',
             'BS':'Baja California Sur',
             'CC':'Campeche',
             'CL':'Coahuila',
             'CM':'Colima',
             'CS':'Chiapas',
             'CH':'Chihuahua',
             'DF':'Ciudad de México',
             'DG':'Durango',
             'GT':'Guanajuato',
             'GR':'Guerrero',
             'HG':'Hidalgo',
             'JC':'Jalisco',
             'MC':'México',
             'MN':'Michoacán',
             'MS':'Morelos',
             'NT':'Nayarit',
             'NL':'Nuevo León',
             'OC':'Oaxaca',
             'PL':'Puebla',
             'QT':'Querétaro',
             'QR':'Quintana Roo',
             'SP':'San Luis Potosí',
             'SL':'Sinaloa',
             'SR':'Sonora',
             'TC':'Tabasco',
             'TS':'Tamaulipas',
             'TL':'Tlaxcala',
             'VZ':'Veracruz',
             'YN':'Yucatán',
             'ZS':'Zacatecas'}

def leer_entidad():
    """Lee la entidad federativa de nacimiento"""
    print('¿En que entidad federativa naciste?\n(2 letras mayúsculas, \
    por ejemplo: DF; ? para ver la lista de entidades)')
    entidad = input('>>>').upper()
    while entidad not in entidades:
        if entidad == '?':
            for clave, valor in entidades.items():
                print(clave, ':', valor)
            print('')
        entidad = input('>>>').upper()
    return entidad


#llamando funciones
def leer_datos():
    """Lee los datos del usuario"""
    nombres = leer_nombres()
    primer_apellido, segundo_apellido = leer_apellidos()
    anio_nacimiento = leer_anio_nacimiento()
    mes_nacimiento = leer_mes_nacimiento()
    dia_nacimiento = leer_dia_nacimiento()
    sexo = leer_sexo()
    entidad = leer_entidad()
    return nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
        mes_nacimiento, dia_nacimiento, sexo, entidad
'''
Recordemos, como se vio hace tiempo, qué se puede manejar el valor del retorno de una función 
como una tupla, es decir como una colección de valores. También vimos que las 
funciones pueden recibir precisamente una tupla, de esta forma realizamos el llamado para el cálculo de la CURP:
'''



def curp(nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
    mes_nacimiento, dia_nacimiento, sexo, entidad):
    """Calcula la CURP"""
    curp = primer_apellido[0:2].upper() + \
        segundo_apellido[0].upper() + \
        nombres[0].upper() + \
        anio_nacimiento[2:4] + \
        mes_nacimiento + \
        dia_nacimiento + \
        sexo + \
        entidad
    return curp




curp_generada =curp(*leer_datos())


# Imprimiendo la CURP calculada en pantalla
print("La CURP generada es:", curp_generada)