def mostrar_info(nombre, edad, *args,  actividad = "Estudiante", **kwargs):
    print(f"Hola: {nombre}, tiene {edad} anios, y es {actividad}")
    print(f"args: {args}")
    print(f"**kwargs: {kwargs}")

mostrar_info("Pablo", 27, "banana", "manzana",Algo=True)