from clases import Persona, Director, Actor, Pelicula
from datetime import datetime
from tuplas import SEXO, devuelve_sexo, ESTILO_PELI, devuelve_estilo
import re


def valida_fecha(titulo):
    while True:
        fecha = input(f'Ingrese una fecha en el formato YYYY-MM-DD para {titulo}: ')
        try:
            fecha_formato = datetime.strptime(fecha, '%Y-%m-%d')
            return fecha_formato
        except ValueError:
            print(f'La {titulo} no está en el formato correcto (YYYY-MM-DD)...!')


def valida_int(titulo):
    while True:
        try:
            num = int(input(f'Ingrese {titulo}'))
            if num >= 0:
                return num
            print('El valor ingresado no es el correcto')
        except:
            print(f'Valor ingresado incorrecto, {titulo}')


def valida_sexo():
    opciones = ['{}. {}'.format(codigo, descripcion) for codigo, descripcion in SEXO]
    v_sexo = [codigo for codigo, _ in SEXO]
    while True:
        sexo = valida_int(f'Sexo, valor numérico {opciones} : ')
        if sexo in v_sexo:
            return sexo
        print(f'El ID del sexo no es el correcto, verificar las opciones {opciones}')


def valida_mail():
    while True:
        email = input('Correo: ')
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        print('Correo incorrecto, ingrese nuevamente.')


def valida_cedula():
    while True:
        cedula = input('Cédula: ')
        persona = Persona.valida_cedula(cedula)
        if persona is None:
            return cedula
        print(f'La cédula {cedula}, ya existe')


def crear_persona():
    print('INGRESO DE DATOS')
    cedula = valida_cedula()
    nombre = input('Nombre: ').upper()
    apellido = input('Apellido: ').upper()
    fecha_nacimiento = valida_fecha('Fecha Nacimiento')
    sexo = valida_sexo()
    email = valida_mail()
    persona = Persona(None, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
    persona.inserta_persona()


def modificar_persona():
    print('MODIFICACIÓN DE DATOS')
    cedula = input('Cédula a modificar: ')
    persona = Persona.valida_cedula(cedula)
    if persona is None:
        print('No existe ninguna persona con esta cédula...!')
        return
    nombre = input('Nombre: ').upper()
    apellido = input('Apellido: ').upper()
    fecha_nacimiento = valida_fecha('Fecha Nacimiento')
    sexo = valida_sexo()
    email = valida_mail()
    persona = Persona(persona[0], cedula, nombre, apellido, fecha_nacimiento, sexo, email)
    persona.actualiza_persona()


def consulta_una_persona():
    print('PRESENTACIÓN DE DATOS')
    cedula = input('Cédula a consultar: ')
    persona = Persona.valida_cedula(cedula)
    if persona is None:
        print('No existe ninguna persona con esta cédula...!')
        return
    sexo = devuelve_sexo(persona[5])
    print('{:<10} {:<10} {:<20} {:<20} {:<15} {:<10} {:<30}'.format('ID', 'CÉDULA', 'NOMBRE', 'APELLIDO',
                                                                    'FECH. NAC.', 'SEXO', 'EMAIL'))
    print('{:<10} {:<10} {:<20} {:<20} {:<15} {:<10} {:<30}'.format(persona[0], persona[1], persona[2], persona[3],
                                                                    str(persona[4]), sexo, persona[6]))


def eliminar_persona():
    print('ELIMINACIÓN DE DATOS')
    cedula = input('Cédula a eliminar: ')
    persona = Persona.valida_cedula(cedula)
    if persona is None:
        print('No existe ninguna persona con esta cédula...!')
        return
    persona = Persona(persona[0], '', '', '', '', '', '')
    persona.eliminar_persona()


def valida_estilo_peli():
    opciones = ['{}. {}'.format(codigo, descripcion) for codigo, descripcion in ESTILO_PELI]
    v_estilo_peli = [codigo for codigo, _ in ESTILO_PELI]
    while True:
        peli = valida_int(f'Estilo Peli, valor numérico {opciones} : ')
        if peli in v_estilo_peli:
            return peli
        print(f'El ID del Estilo Peli no es el correcto, verificar las opciones {opciones}')

def consulta_un_director():
    print('PRESENTACIÓN DE DATOS')
    cedula = input('Cédula a consultar: ')
    director = Director.valida_director(cedula)
    if director is None:
        print('No existe DIRECTOR con esta cédula...!')
        return
    estilo = devuelve_estilo(director[2])
    print('{:<10} {:<30} {:<20} {:<15} {:<20} {:<10} {:<30}'.format('CÉDULA', 'DIRECTOR', 'EMAIL', 'PELI. DIR.',
                                                                    'ESTILO PELI', 'PREMIOS', 'BIOGRAFÍA'))
    print('{:<10} {:<30} {:<20} {:<15} {:<20} {:<10} {:<30}'.format(director[6], director[7] + ' ' + director[8], director[11],
                                                                    director[1], estilo, director[3], director[4]))


def crear_director():
    print('INGRESO DE DATOS')
    cedula = input('Cédula:')
    director = Director.valida_director(cedula)
    if director is None:
        persona = Persona.valida_cedula(cedula)
        if persona is None:
            print('No existe ninguna persona con esta cédula...!')
            return
        num_peliculas_dirigidas = valida_int('Num. Películas Dirigidas:')
        estilo_director = valida_estilo_peli()
        premios_ganados = valida_int('Premios ganados:')
        biografia = input('Biografía').upper()
        director = Director(persona[0], persona[1], persona[2], persona[3], persona[4], persona[5], persona[6],
                            num_peliculas_dirigidas,
                            estilo_director, premios_ganados, biografia)
        director.inserta_director()
    print('Ya existe Director registrado...!')
    return


def modificar_director():
    print('MODIFICACIÓN DE DATOS')
    cedula = input('Cédula:')
    director = Director.valida_director(cedula)
    if director is None:
        print('No existe Director con esta cédula para modificar...!')
        return
    num_peliculas_dirigidas = valida_int('Num. Películas Dirigidas:')
    estilo_director = valida_estilo_peli()
    premios_ganados = valida_int('Premios ganados:')
    biografia = input('Biografía: ').upper()
    director = Director(director[0], '', '', '', '', '', '', num_peliculas_dirigidas, estilo_director, premios_ganados,
                        biografia)
    director.modifica_director()

def eliminar_director():
    print('ELIMINACIÓN DE DATOS')
    cedula = input('Cédula:')
    director = Director.valida_director(cedula)
    if director is None:
        print('No existe Director con esta cédula para eliminar...!')
        return
    director = Director(director[0], '', '', '', '', '', '', '', '', '', '')
    director.eliminar_director()

def crear_actor():
    print('INGRESO DE DATOS')
    cedula = input('Cédula:')
    actor = Actor.valida_actor(cedula)
    if actor is None:
        persona = Persona.valida_cedula(cedula)
        if persona is None:
            print('No existe ninguna persona con esta cédula...!')
            return
        print(persona[2], persona[3],'\n')
        num_peliculas = valida_int('Num. Películas:')
        premios_ganados = valida_int('Premios ganados:')
        biografia = input('Biografía').upper()
        actor = Actor(persona[0], persona[1], persona[2], persona[3], persona[4], persona[5], persona[6],
                            num_peliculas, premios_ganados, biografia)
        actor.inserta_actor()
    print('Ya existe ACTOR registrado...!')
    return

def modificar_actor():
    print('MODIFICACIÓN DE DATOS')
    cedula = input('Cédula:')
    actor = Actor.valida_actor(cedula)
    if actor is None:
        print('No existe Actor con esta cédula para modificar...!')
        return
    num_peliculas = valida_int('Num. Películas:')
    premios_ganados = valida_int('Premios ganados:')
    biografia = input('Biografía: ').upper()
    actor = Actor(actor[0], '', '', '', '', '', '', num_peliculas, premios_ganados, biografia)
    actor.modifica_actor()

def eliminar_actor():
    print('ELIMINACIÓN DE DATOS')
    cedula = input('Cédula:')
    actor = Actor.valida_actor(cedula)
    if actor is None:
        print('No existe Director con esta cédula para eliminar...!')
        return
    actor = Actor(actor[0], '', '', '', '', '', '', '', '', '')
    actor.eliminar_actor()

def consulta_un_actor():
    print('PRESENTACIÓN DE DATOS')
    cedula = input('Cédula a consultar: ')
    actor = Actor.valida_actor(cedula)
    if actor is None:
        print('No existe ACTOR con esta cédula...!')
        return

    print('{:<10} {:<30} {:<20} {:<15} {:<10} {:<30}'.format('CÉDULA', 'ACTOR', 'EMAIL', 'NUM. PELI.',
                                                                    'PREMIOS', 'BIOGRAFÍA'))
    print('{:<10} {:<30} {:<20} {:<15} {:<10} {:<30}'.format(actor[5], actor[6] + ' ' + actor[7], actor[10],
                                                                        actor[1], actor[2], actor[3]))

def valida_persona_peli(tipo_persona):
    while True:
        cedula = input(f'Cédula para {tipo_persona}: ')
        if tipo_persona == 'Director':
            d_p = Director.valida_director(cedula)
        else:
            d_p = Actor.valida_actor(cedula)
        if d_p is None:
            print(f'No existe un {tipo_persona} con esa cédula')
            continue
        return d_p[0]

##id, titulo, fecha_estreno, director_id, genero, actor_id
def crear_pelicula():
    print('INGRESO DE DATOS')
    titulo = input('Nombre Película:').upper()
    fecha_estreno = valida_fecha('Fecha Estreno')
    director_id = valida_persona_peli('Director')
    genero = valida_estilo_peli()
    actor_id = valida_persona_peli('Actor')
    pelicula = Pelicula(None, titulo, fecha_estreno, director_id, genero, actor_id)
    pelicula.inserta_pelicula()


def opcion_menu(titulo, ms):
    while True:
        while True:
            print(f'** OPCIÓN {titulo.upper()} **')
            print(f'1. Crear {titulo}')
            print(f'2. Modificar {titulo}')
            print(f'3. Eliminar {titulo}')
            print(f'4. {titulo} consultar Todos')
            print(f'5. {titulo} consultar uno')
            print(f'6. Regresar al menú principal')
            try:
                opc = int(input(f'Seleccione una opción del menú {titulo} (1-6):'))
                if 1 <= opc <= 6:  # AND
                    break
            except:
                print('Por favor, seleccione una opción correcta (1-6)...!')

        if opc == 6:
            main_menu()
        elif ms == 1:
            if opc == 1:
                crear_persona()
            elif opc == 2:
                modificar_persona()
            elif opc == 3:
                eliminar_persona()
            elif opc == 4:
                Persona.lista_personas()
            else:
                consulta_una_persona()
        elif ms == 2:
            if opc == 1:
                crear_director()
            elif opc == 2:
                modificar_director()
            elif opc == 3:
                eliminar_director()
            elif opc == 4:
                Director.lista_directores()
            else:
                consulta_un_director()
        elif ms == 3:
            if opc == 1:
                crear_actor()
            elif opc == 2:
                modificar_actor()
            elif opc == 3:
                eliminar_actor()
            elif opc == 4:
                Actor.lista_actores()
            else:
                consulta_un_actor()
        elif ms == 4:
            if opc == 1:
                crear_pelicula()
            elif opc == 2:
                pass  # proceso de modificar pelicula
            elif opc == 3:
                pass  # proceso de eliminar pelicula
            elif opc == 4:
                Pelicula.lista_peliculas()
            else:
                pass  # proceso de consul. una pelicula


def main_menu():
    while True:
        print('** MENÚ DEL SISTEMA **')
        print('1. Persona')  # insertar, modificar, eliminar, consultar todos, consultar uno
        print('2. Director')  # insertar, modificar, eliminar, consultar todos, consultar uno
        print('3. Actor')  # insertar, modificar, eliminar, consultar todos, consultar uno
        print('4. Películas')  # insertar, modificar, eliminar, consultar todos, consultar uno
        print('5. Salir')
        try:
            opc = int(input('Seleccione una opción del menú (1-5):'))
            if 1 <= opc <= 5:  # AND
                break
        except:
            print('Por favor, seleccione una opción correcta (1-5)...!')

    if opc == 1:
        opcion_menu('Persona', opc)
    elif opc == 2:
        opcion_menu('Director', opc)
    elif opc == 3:
        opcion_menu('Actor', opc)
    elif opc == 4:
        opcion_menu('Películas', opc)
    else:
        print('Cerrar sesión...!', opc)
        exit()
