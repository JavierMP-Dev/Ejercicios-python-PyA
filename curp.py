# Lista de palabras prohibidas
#se agregara una funcion que va comparar la curp generada con esta lista de palabras
#si se llega a encontarar que se genero una de estas, se va reeemplazar el 4to caracter por una x
palabras_prohibidas = ["PUTA", "PUTO", "JOTO", "VACA", "COLA", "PITO", "PITA"]

# función para leer nombres 
def leer_nombres():
    """Lee los nombres"""
    print('¿Cuáles son tus nombres? (Mayúsculas y sin acentos)')
    nombres = input('>>>').strip().split()
    
    if nombres:
        primer_nombre = nombres[0].upper()
        if primer_nombre in ["MARIA", "JOSE"]:
            if len(nombres) > 1:
                return nombres[1].upper()
            else:
                return ""
        else:
            return primer_nombre
    else:
        return ""

# función solicitar apellidos 
def leer_apellidos():
    """Lee los apellidos"""
    print('¿Cuáles son tus apellidos? (Mayúsculas y sin acentos)')
    primer_apellido = input('Primer apellido: ').upper()
    segundo_apellido = input('Segundo apellido: ').upper()
    return primer_apellido, segundo_apellido

# Fecha de nacimiento
def leer_anio_nacimiento():
    """Lee el año de nacimiento"""
    print('¿En qué año naciste? (4 dígitos)')
    anio_nacimiento = input('>>>')
    while not anio_nacimiento.isnumeric() or len(anio_nacimiento) != 4 or \
          int(anio_nacimiento) < 1900 or int(anio_nacimiento) > 2024:
        print('Año incorrecto. Debe ser mayor que 1900 y menor que 2024.')
        anio_nacimiento = input('>>>')
    return anio_nacimiento

# Mes de nacimiento
def leer_mes_nacimiento():
    """Lee el mes de nacimiento"""
    print('Enero   -----> 01')
    print('Febrero -----> 02')
    print('Marzo   -----> 03')
    print('Abril   -----> 04')
    print('Mayo    -----> 05')
    print('Junio   -----> 06')
    print('Julio   -----> 07')
    print('Agosto  -----> 08')
    print('Septiembre --> 09')
    print('Octubre -----> 10')
    print('Noviembre----> 11')
    print('Diciembre----> 12')
    print('¿En qué mes naciste? (2 dígitos)')
    mes_nacimiento = input('>>>')
    while not mes_nacimiento.isnumeric() or len(mes_nacimiento) != 2 or \
          int(mes_nacimiento) < 1 or int(mes_nacimiento) > 12:
        print('Mes incorrecto. Debe ser un número del 1 al 12.')
        mes_nacimiento = input('>>>')
    return mes_nacimiento

# Día de nacimiento
def leer_dia_nacimiento():
    """Lee el día de nacimiento"""
    print('¿En qué día naciste?  (2 dígitos)')
    dia_nacimiento = input('>>>')
    while not dia_nacimiento.isnumeric() or len(dia_nacimiento) != 2:
        dia_nacimiento = input('>>>')
    return dia_nacimiento

# Leer sexo
def leer_sexo():
    """Lee el sexo"""
    print('¿Cuál es tu sexo? (H/M)')
    sexo = input('>>>').upper()
    while sexo not in ['H', 'M', 'X']:
        sexo = input('>>>').upper()
    return sexo

# Entidades federativas
entidades = {'AG':'Aguascalientes', 'BC':'Baja California', 'BS':'Baja California Sur', 'CC':'Campeche',
             'CL':'Coahuila', 'CM':'Colima', 'CS':'Chiapas', 'CH':'Chihuahua', 'DF':'Ciudad de México',
             'DG':'Durango', 'GT':'Guanajuato', 'GR':'Guerrero', 'HG':'Hidalgo', 'JC':'Jalisco',
             'MC':'México', 'MN':'Michoacán', 'MS':'Morelos', 'NT':'Nayarit', 'NL':'Nuevo León',
             'OC':'Oaxaca', 'PL':'Puebla', 'QT':'Querétaro', 'QR':'Quintana Roo', 'SP':'San Luis Potosí',
             'SL':'Sinaloa', 'SR':'Sonora', 'TC':'Tabasco', 'TS':'Tamaulipas', 'TL':'Tlaxcala',
             'VZ':'Veracruz', 'YN':'Yucatán', 'ZS':'Zacatecas'}

def leer_entidad():
    """Lee la entidad federativa de nacimiento"""
    entidad = ''
    while entidad not in entidades:
        print('¿En qué entidad federativa naciste?\n(2 letras mayúsculas, \
        por ejemplo: DF; ? para ver la lista de entidades)')
        entidad = input('>>>').upper()
        if entidad == '?':
            for clave, valor in entidades.items():
                print(clave, ':', valor)
            print('')
    return entidad

# Llamando funciones que recaban datos
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

#tupla despues de recibir datos a traves de funciones
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
    
    # Verificar si las primeras cuatro letras coinciden con alguna palabra prohibida
    #en caso de encontrar una coinicidencia reemplazazr la ultima letra por una x
    if curp[:4] in palabras_prohibidas:
        curp = curp[:3] + 'X' + curp[4:]
    
    return curp

curp_generada = curp(*leer_datos())

# Imprimiendo la CURP calculada en pantalla
print("La CURP generada es:", curp_generada)
