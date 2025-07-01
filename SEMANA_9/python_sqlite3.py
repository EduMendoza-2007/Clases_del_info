import sqlite3
import uuid
import datetime

conn = sqlite3.connect('blog.db')

cursor = conn.cursor()

def crear_tablas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                   uuid VARCHAR PRIMARY KEY,
                   username VARCHAR UNIQUE NOT NULL,
                   email VARCHAR UNIQUE NOT NULL,
                   password VARCHAR NOT NULL,
                   created_at TIMESTAMP NOT NULL)''')
    
    #categorias
    #posts
    #comentarios

def insertar_usuario():
    username = input('Inserte nombre de usuario: ').strip()
    email = input('Inserte email de usuario: ').strip()
    password = input('Inserte password de usuario: ')
    
    #validacion

    #proceso
    #enciptar password
    user_uuid = uuid.uuid4()
    created_at = datetime.datetime.now()

    query = f'''INSERT INTO usuarios (uuid, username, email, password, created_at)
        VALUES (?, ?, ?, ?, ?)'''
    
    cursor.execute(
        query, (str(user_uuid), username, email, password, created_at))

    conn.commit()
    
    print('Usuario registrado correctamente.')
    #populo en la db




def insertar_post():
    pass

def insertar_categoria():
    pass

def listar_usuarios():
    pass

def listar_posts():
    pass

def listar_categorias():
    pass

def cerrar_conexion():
     cursor.close()
     conn.close()

def menu():
    crear_tablas()
    while True:
        print('Menu')
        print('1. Insertar un usuario')
        print('2. Insertar un post')
        print('3. Insertar una categoria')
        print('4. Listar usuarios')
        print('5. Listar post')
        print('6. Listar categorias')
        print('0. Salir')

        opcion = input('Seleccione una opcion: ')

        if (opcion == '1'):
            insertar_usuario()
        elif (opcion == '2'):
            insertar_post()    
        elif (opcion == '3'):
            insertar_categoria()
        elif (opcion == '4'):
            listar_usuarios()
        elif (opcion == '5'):
            listar_posts()
        elif (opcion == '6'):
            listar_categorias()
        elif (opcion == '0'):
            break
        else:
            print('Opcion no valida intente nuevamente')
                        

menu()