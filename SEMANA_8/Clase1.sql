CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	contenido TEXT NOT NULL,
	fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM posts;

CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	contrasenia VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (nombre, email, contrasenia)
VALUES
	('Edu', 'mendozaeduardoomar@email.com', 'facil123'),
	('Pablo', 'pabli@email.com', 'facil123');

SELECT * FROM usuarios;

ALTER TABLE posts
ADD COLUMN usuario_id INT REFERENCES usuarios(id);

INSERT INTO posts (titulo, contenido)
VALUES
	('Primer posts', 'La vida como programador'),
	('Segundo posts', 'Agarra la pala');

ALTER TABLE posts
ALTER COLUMN usuario_id SET NOT NULL;

UPDATE posts
SET usuario_id = 2
WHERE id = 1;

UPDATE posts
SET usuario_id = 2
WHERE id = 2;

INSERT INTO posts (titulo, contenido, usuario_id)
VALUES
	('Tercer post', 'La vida de un programador',1);

CREATE TYPE user_status_enum AS ENUM ('ACTIVO', 'INACTIVO', 'PENDIENTE');

ALTER TABLE usuarios
ADD COLUMN estado user_status_enum DEFAULT 'PENDIENTE';