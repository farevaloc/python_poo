CREATE DATABASE IF NOT EXISTS gestion_peliculas;
USE gestion_peliculas;

DROP TABLE IF EXISTS personas;
CREATE TABLE IF NOT EXISTS personas (
  id int(11) NOT NULL AUTO_INCREMENT,
  cedula varchar(10) NOT NULL,
  nombre varchar(255) DEFAULT NULL,
  apellido varchar(255) DEFAULT NULL,
  fecha_nacimiento date DEFAULT NULL,
  sexo int(11) DEFAULT NULL,
  email varchar(255) DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY cedula (cedula)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS actores;
CREATE TABLE IF NOT EXISTS actores (
  id int(11) NOT NULL,
  num_peliculas int(11) DEFAULT NULL,
  premios_ganados int(11) DEFAULT NULL,
  biografia text,
  PRIMARY KEY (id),
  CONSTRAINT actores_ibfk_1 FOREIGN KEY (id) REFERENCES personas (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS directores;
CREATE TABLE IF NOT EXISTS directores (
  id int(11) NOT NULL,
  num_peliculas_dirigidas int(11) DEFAULT NULL,
  estilo_director int(11) DEFAULT NULL,
  premios_ganados int(11) DEFAULT NULL,
  biografia text,
  PRIMARY KEY (id),
  CONSTRAINT directores_ibfk_1 FOREIGN KEY (id) REFERENCES personas (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS peliculas;
CREATE TABLE IF NOT EXISTS peliculas (
  id int(11) NOT NULL AUTO_INCREMENT,
  titulo varchar(255) DEFAULT NULL,
  fecha_estreno date DEFAULT NULL,
  director_id int(11) DEFAULT NULL,
  genero int(11) DEFAULT NULL,
  actor_id int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY director_id (director_id),
  KEY actor_id (actor_id),
  CONSTRAINT FK_peliculas_actores FOREIGN KEY (actor_id) REFERENCES actores (id),
  CONSTRAINT peliculas_ibfk_1 FOREIGN KEY (director_id) REFERENCES directores (id)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

