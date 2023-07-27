def devuelve_sexo(valor):
    for codigo, desc in SEXO:
        if valor == codigo:
            sexo = desc
            return sexo

def devuelve_estilo(valor):
    for codigo, desc in ESTILO_PELI:
        if valor == codigo:
            peli = desc
            return peli


SEXO = (
    (1, 'MASCULINO'),
    (2, 'FEMENINO'),
)

ESTILO_PELI = (
    (1, 'ACCIÓN'),
    (2, 'AVENTURA'),
    (3, 'COMEDIA'),
    (4, 'DRAMA'),
    (5, 'TERROR'),
    (6, 'SUSPENSO'),
    (7, 'CIENCIA FICCIÓN'),
    (8, 'ROMANCE'),
    (9, 'FANTASÍA'),
    (10, 'ANIMACIÓN'),
)