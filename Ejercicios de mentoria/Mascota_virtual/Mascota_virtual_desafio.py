# importar el modulo random
import random
# import imagen desde el archivo mascota.py
from Mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 0
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_muerte = imagen.muerto
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz

    def alimentar(self):
        self.hambre -= random.randint(10,15)
        print(f"{self.nombre}, ya fue alimentado")
        self.felicidad -= random.randint(5,10)

        if self.felicidad < 0:
            self.felicidad == 0
        if self.hambre < 0:
            self.hambre == 0
        if self.hambre == 0:
            print(imagen.disgustado)
            print(f"{self.nombre}, esta lleno, no quiere mas")


    def jugar(self):
        if self.hambre < 70:
            self.felicidad += random.randint(10,25)
            self.hambre += random.randint(10,15)
            print(f"{self.nombre} se esta divirtiendo")
        elif self.hambre > 100:
            self.hambre == 100 
        else:
            print(f"Si alimentas a {self.nombre}, va a seguir jugando, porque ahora tiene hambre")       
        if self.felicidad > 100:
            self.felicidad == 100

    def estado_animo(self):
        pass

    def presentacion(self):  # opcional
        pass

    def despedida(self):  # opcional
        pass


# Crear una instancia de MascotaVirtual

# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉
# interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
# interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"
