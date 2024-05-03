def siguiente_consonante(palabra):
    """Busca la primera consonante de una palabra"""
    for letra in palabra:
        if letra not in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def siguiente_vocal(palabra):
    """Busca la primera vocal de una palabra"""
    for letra in palabra:
        if letra in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def curp_parte_1(primer_apellido, segundo_apellido, nombres):
    """Calcula la primera parte de la CURP"""
    curp = primer_apellido[0:1] + siguiente_vocal(primer_apellido[1:]) + segundo_apellido[0:1] + nombres[0:1]
    return curp

def curp_parte_2(anio_nacimiento, mes_nacimiento, dia_nacimiento):
    """Calcula la segunda parte de la CURP"""
    curp = anio_nacimiento[2:4] + mes_nacimiento + dia_nacimiento
    return curp

def primera_consonante(palabra):
    """Busca la primera consonante de una palabra"""
    for letra in palabra:
        if letra not in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'


def curp_parte_5(primer_apellido, segundo_apellido, nombres):
    """Calcula la quinta parte de la CURP"""
    curp = primera_consonante(primer_apellido[1:]) + \
        siguiente_consonante(segundo_apellido[1:]) + \
        siguiente_consonante(nombres[1:])
    return curp

def curp(nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
    mes_nacimiento, dia_nacimiento, sexo, entidad):
    """Calcula la CURP"""
    curp = curp_parte_1(primer_apellido, segundo_apellido, nombres) + \
        curp_parte_2(anio_nacimiento, mes_nacimiento, dia_nacimiento) + \
        sexo + entidad + \
        curp_parte_5(primer_apellido, segundo_apellido, nombres) + 'XX'
    return curp