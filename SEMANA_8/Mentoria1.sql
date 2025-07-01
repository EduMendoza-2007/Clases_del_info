CREATE TABLE usuarios(
	id_usuario SERIAL PRIMARY KEY,
	email VARCHAR(50) UNIQUE NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	fecha_nacimiento DATE,
	pais VARCHAR(30)
);

SELECT * FROM usuarios;

CREATE TABLE peliculas(
	id_pelicula SERIAL PRIMARY KEY,
	titulo VARCHAR(150) NOT NULL,
	genero VARCHAR(50),
	duracion INT
);

SELECT * FROM peliculas;

CREATE TYPE modo_visualizacion_enum AS ENUM ('ONLINE', 'DESCARGADA');

CREATE TABLE alquileres(
	id_alquiler SERIAL PRIMARY KEY,
	id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario),
	id_pelicula INTEGER NOT NULL REFERENCES peliculas(id_pelicula),
	fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	precio DECIMAL(10, 2),
	modo_visualizacion modo_visualizacion_enum NOT NULL
);

SELECT * FROM alquileres;

INSERT INTO usuarios(email, nombre, fecha_nacimiento, pais) VALUES
('ana@gmail.com', 'Ana López', '1995-03-12', 'Argentina'),
('marcos@mail.com', 'Marcos Díaz', '1988-07-21', 'Chile');

INSERT INTO peliculas(titulo, genero, duracion) VALUES
('Matrix', 'Ciencia Ficción', 136),
('El Padrino', 'Drama', 175);

INSERT INTO alquileres(id_usuario, id_pelicula, precio, modo_visualizacion) VALUES
(1, 1, 450.00, 'ONLINE'),
(2, 2, 550.00, 'DESCARGADA');