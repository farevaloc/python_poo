import mysql.connector
from tuplas import devuelve_sexo, devuelve_estilo


class Persona:
    def __init__(self, id, cedula, nombre, apellido, fecha_nacimiento, sexo, email):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.email = email

    def eliminar_persona(self):
        db = ConexionDB()
        query = 'DELETE FROM personas WHERE id = %s;'
        opc = input('¿Está seguro que desea eliminar el registro? (S/N):').upper()
        if opc != 'S':
            print('Eliminación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        try:
            db.delete(query, (self.id,))
        except mysql.connector.Error as e:
            print('Error:', e)
        finally:
            db.cerrar_conexion()

    def actualiza_persona(self):
        db = ConexionDB()
        query = 'UPDATE personas SET nombre=%s, apellido=%s, fecha_nacimiento=%s, sexo=%s, email=%s WHERE id = %s;'
        opc = input('¿Está seguro que desea actualizar el registro? (S/N):').upper()
        if opc != 'S':
            print('Modificación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        db.update(query, (self.nombre, self.apellido, self.fecha_nacimiento, self.sexo, self.email, self.id))
        db.cerrar_conexion()

    def inserta_persona(self):
        db = ConexionDB()
        query = 'INSERT INTO personas (cedula, nombre, apellido, fecha_nacimiento, sexo, email) ' \
                'VALUES (%s, %s, %s, %s, %s, %s)'
        db.insert(query, (self.cedula, self.nombre, self.apellido, self.fecha_nacimiento, self.sexo, self.email))
        db.cerrar_conexion()

    @staticmethod
    def valida_cedula(cedula):
        db = ConexionDB()
        query = 'SELECT * FROM personas WHERE cedula = %s;'
        resultado = db.fetch_one(query, (cedula,))
        db.cerrar_conexion()
        return resultado

    @staticmethod
    def lista_personas():
        db = ConexionDB()
        query = 'SELECT * FROM personas;'
        resultado = db.fetch_all(query)  # [(),(),()]
        db.cerrar_conexion()
        if not resultado:
            print('No hay registros de personas...!')
            return
        # id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        print('{:<10} {:<10} {:<20} {:<20} {:<15} {:<10} {:<30}'.format('ID', 'CÉDULA', 'NOMBRE', 'APELLIDO',
                                                                        'FECH. NAC.', 'SEXO', 'EMAIL'))

        for info in resultado:
            sexo = devuelve_sexo(info[5])
            print('{:<10} {:<10} {:<20} {:<20} {:<15} {:<10} {:<30}'.format(info[0], info[1], info[2], info[3],
                                                                            str(info[4]), sexo, info[6]))


class Actor(Persona):
    def __init__(self, id, cedula, nombre, apellido, fecha_nacimiento, sexo, email, num_peliculas,
                 premios_ganados, biografia):
        Persona.__init__(self, id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        self.num_peliculas = num_peliculas
        self.premios_ganados = premios_ganados
        self.biografia = biografia

    @staticmethod
    def valida_actor(cedula):
        db = ConexionDB()
        query = 'SELECT * FROM actores INNER JOIN personas ON actores.id= personas.id WHERE personas.cedula= %s;'
        resultado = db.fetch_one(query, (cedula,))
        db.cerrar_conexion()
        return resultado

    def inserta_actor(self):
        db = ConexionDB()
        query = 'INSERT INTO actores (id, num_peliculas, premios_ganados, biografia) ' \
                'VALUES (%s, %s, %s, %s);'
        db.insert(query,
                  (self.id, self.num_peliculas, self.premios_ganados, self.biografia))
        db.cerrar_conexion()

    def modifica_actor(self):
        db = ConexionDB()
        query = 'UPDATE actores SET num_peliculas=%s, premios_ganados=%s, biografia=%s WHERE id=%s;'
        opc = input('¿Está seguro que desea actualizar el registro? (S/N):').upper()
        if opc != 'S':
            print('Modificación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        db.update(query,
                  (self.num_peliculas, self.premios_ganados, self.biografia, self.id))
        db.cerrar_conexion()

    def eliminar_actor(self):
        db = ConexionDB()
        query = 'DELETE FROM actores WHERE id = %s;'
        opc = input('¿Está seguro que desea eliminar el registro? (S/N):').upper()
        if opc != 'S':
            print('Eliminación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        try:
            db.delete(query, (self.id,))
        except mysql.connector.Error as e:
            print('Error:', e)
        finally:
            db.cerrar_conexion()

    @staticmethod
    def lista_actores():
        db = ConexionDB()
        query = "SELECT p.cedula, CONCAT(p.nombre,' ',p.apellido), p.email,a.num_peliculas, " \
                "a.premios_ganados, a.biografia FROM actores AS a INNER JOIN personas AS p ON a.id=p.id "
        resultado = db.fetch_all(query)  # [(),(),()]
        db.cerrar_conexion()
        if not resultado:
            print('No hay registros de actores...!')
            return
        # id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        print('{:<10} {:<30} {:<20} {:<15} {:<10} {:<30}'.format('CÉDULA', 'ACTOR', 'EMAIL', 'NUM. PELI.',
                                                                 'PREMIOS', 'BIOGRAFÍA'))

        for info in resultado:
            print('{:<10} {:<30} {:<20} {:<15} {:<10} {:<30}'.format(info[0], info[1], info[2],
                                                                     info[3], info[4],
                                                                     info[5]))


# id, num_peliculas_dirigidas, estilo_director, premios_ganados, biografia
class Director(Persona):
    def __init__(self, id, cedula, nombre, apellido, fecha_nacimiento, sexo, email, num_peliculas_dirigidas,
                 estilo_director, premios_ganados, biografia):
        super().__init__(id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        self.num_peliculas_dirigidas = num_peliculas_dirigidas
        self.estilo_director = estilo_director
        self.premios_ganados = premios_ganados
        self.biografia = biografia

    def inserta_director(self):
        db = ConexionDB()
        query = 'INSERT INTO directores (id, num_peliculas_dirigidas, estilo_director, premios_ganados, biografia) ' \
                'VALUES (%s, %s, %s, %s, %s);'
        db.insert(query,
                  (self.id, self.num_peliculas_dirigidas, self.estilo_director, self.premios_ganados, self.biografia))
        db.cerrar_conexion()

    def modifica_director(self):
        db = ConexionDB()
        query = 'UPDATE directores SET num_peliculas_dirigidas=%s, estilo_director=%s, premios_ganados=%s, biografia=%s WHERE id=%s;'
        opc = input('¿Está seguro que desea actualizar el registro? (S/N):').upper()
        if opc != 'S':
            print('Modificación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        db.update(query,
                  (self.num_peliculas_dirigidas, self.estilo_director, self.premios_ganados, self.biografia, self.id))
        db.cerrar_conexion()

    def eliminar_director(self):
        db = ConexionDB()
        query = 'DELETE FROM directores WHERE id = %s;'
        opc = input('¿Está seguro que desea eliminar el registro? (S/N):').upper()
        if opc != 'S':
            print('Eliminación cancelada por el usuario...!')
            db.cerrar_conexion()
            return
        try:
            db.delete(query, (self.id,))
        except mysql.connector.Error as e:
            print('Error:', e)
        finally:
            db.cerrar_conexion()

    @staticmethod
    def valida_director(cedula):
        db = ConexionDB()
        query = 'SELECT * FROM directores INNER JOIN personas ON directores.id= personas.id WHERE personas.cedula= %s;'
        resultado = db.fetch_one(query, (cedula,))
        db.cerrar_conexion()
        return resultado

    @staticmethod
    def lista_directores():
        db = ConexionDB()
        query = "SELECT personas.cedula, CONCAT(personas.nombre, ' ', personas.apellido), personas.email, " \
                "directores.num_peliculas_dirigidas, directores.estilo_director, directores.premios_ganados, " \
                "directores.biografia FROM directores INNER JOIN personas ON directores.id= personas.id;"
        resultado = db.fetch_all(query)  # [(),(),()]
        db.cerrar_conexion()
        if not resultado:
            print('No hay registros de directores...!')
            return
        # id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        print('{:<10} {:<30} {:<20} {:<15} {:<20} {:<10} {:<30}'.format('CÉDULA', 'DIRECTOR', 'EMAIL', 'PELI. DIR.',
                                                                        'ESTILO PELI', 'PREMIOS', 'BIOGRAFÍA'))

        for info in resultado:
            estilo = devuelve_estilo(info[4])
            print('{:<10} {:<30} {:<20} {:<15} {:<20} {:<10} {:<30}'.format(info[0], info[1], info[2],
                                                                            info[3], estilo, info[5],
                                                                            info[6]))


# id, titulo, fecha_estreno, director_id, genero, actor_id
class Pelicula:
    def __init__(self, id, titulo, fecha_estreno, director_id, genero, actor_id):
        self.id = id
        self.titulo = titulo
        self.fecha_estreno = fecha_estreno
        self.director_id = director_id
        self.genero = genero
        self.actor_id = actor_id

    def inserta_pelicula(self):
        db = ConexionDB()
        query = 'INSERT INTO peliculas (titulo, fecha_estreno, director_id, genero, actor_id) VALUES (%s, %s, %s, %s, %s);'
        db.insert(query, (self.titulo, self.fecha_estreno, self.director_id, self.genero, self.actor_id))
        db.cerrar_conexion()

    @staticmethod
    def lista_peliculas():
        db = ConexionDB()
        query = "SELECT p.titulo, p.fecha_estreno, p.genero,concat(dp.nombre, ' ', dp.apellido) AS Director, " \
                "d.biografia AS BioDirector,concat(ap.nombre, ' ', ap.apellido) AS Actor,a.biografia AS Actor " \
                "FROM peliculas AS p INNER JOIN directores AS d ON p.director_id=d.id " \
                "INNER JOIN personas AS dp ON d.id=dp.id INNER JOIN actores AS a ON p.actor_id=a.id " \
                "INNER JOIN personas AS ap ON a.id=ap.id;"
        resultado = db.fetch_all(query)  # [(),(),()]
        db.cerrar_conexion()
        if not resultado:
            print('No hay registros de películas...!')
            return
        # id, cedula, nombre, apellido, fecha_nacimiento, sexo, email)
        print('{:<25} {:<10} {:<20} {:<25} {:<25} {:<25} {:<25}'.format('TÍTULO', 'FECHA EST.', 'GÉNERO', 'DIRECTOR',
                                                                        'BIO DIRECT.', 'ACTOR', 'BIO ACTOR'))

        for info in resultado:
            estilo = devuelve_estilo(info[2])
            print('{:<25} {:<10} {:<20} {:<25} {:<25} {:<25} {:<25}'.format(info[0], str(info[1]), estilo,
                                                                            info[3], info[4], info[5],
                                                                            info[6]))


class ConexionDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='user_gestion',
            password='emelec2023',
            database='gestion_peliculas'
        )
        self.cursor = self.conexion.cursor()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, parms):
        self.cursor.execute(query, parms)
        return self.cursor.fetchone()

    def delete(self, query, parms):
        try:
            self.cursor.execute(query, parms)
            self.conexion.commit()
            print('Registro eliminado exitosamente...!')
        except mysql.connector.Error as e:
            print('Error:', e)

    def update(self, query, parms):
        try:
            self.cursor.execute(query, parms)
            self.conexion.commit()
            print('Registro actualizado exitosamente...!')
        except mysql.connector.Error as e:
            print('Error:', e)

    def insert(self, query, parms):
        try:
            self.cursor.execute(query, parms)
            self.conexion.commit()
            print('Registro guardado exitosamente...!')
        except mysql.connector.IntegrityError as e:
            print('Error:', e)

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
