from carpeta_a.modulos import saludar as saludo
from carpeta_a.modulos_b import despedir as despedir

def ejecutar():
    mensaje = saludo("Pablo")
    print(f"modulo_b recibido: {mensaje}")

    mensaje_despedida = despedir("Juan")
    print(f"desde modulo_b: {mensaje_despedida}")

ejecutar()