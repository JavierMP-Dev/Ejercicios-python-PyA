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
    print('¿En qué entidad federativa naciste?\n(2 letras mayúsculas, '
          'por ejemplo: DF; ? para ver la lista de entidades)')
    entidad = input('>>>').upper()
    while entidad not in entidades:
        if entidad == '?':
            for clave, valor in entidades.items():
                print(clave, ':', valor)
            print('')
        entidad = input('>>>').upper()
    return entidad

def generar_curp():
    """Genera la CURP del usuario"""
    nombre = input('Ingresa tu(s) nombre(s): ').upper()
    apellido_paterno = input('Ingresa tu apellido paterno: ').upper()
    apellido_materno = input('Ingresa tu apellido materno: ').upper()
    dia_nacimiento = input('Ingresa tu día de nacimiento (2 dígitos): ')
    mes_nacimiento = input('Ingresa tu mes de nacimiento (2 dígitos): ')
    anio_nacimiento = input('Ingresa tu año de nacimiento (4 dígitos): ')
    sexo = input('Ingresa tu sexo (H para hombre, M para mujer): ').upper()

    entidad = leer_entidad()

    # Generación de la CURP
    curp = apellido_paterno[:2] + apellido_materno[0] + nombre[0] + \
           anio_nacimiento[2:] + mes_nacimiento + dia_nacimiento + sexo + entidad
    return curp

# Ejemplo de uso
print('Generador de CURP\n')
curp_generada = generar_curp()
print('\nTu CURP es:', curp_generada)
