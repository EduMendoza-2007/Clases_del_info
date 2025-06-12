class Vehiculos:
    def __init__(self,marca, modelo, estado, wuau ):
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        self.color = wuau


    def mostrar_info(self):
        print(f"Tengo un/una {self.marca} - {self.modelo} en un estado {self.estado} de color {self.color}")


class Auto(Vehiculos):
    def __init__(self, marca, modelo, estado, wuau, numero_puertas, tipo_combustible):
        super().__init__(marca, modelo, estado, wuau)
        self.puertas = numero_puertas
        self.combustible = tipo_combustible
    
    def mostrar_info(self):
        print(
              f"Tengo un/una {self.marca} - {self.modelo} en un estado {self.estado} de color {self.color} con {self.puertas} y con motor {self.combustible}")


moto = Vehiculos("Honda", "Wave", "Nuevito", "Rojo")
auto = Auto("Toyota", "Yaris GR", "Impecable(joya nunca taxi)", "Negro", 4, "Naftero")
camion = Vehiculos("Mercedes", "1114", "Se defiende", "Rojo")

mis_vehiculos = [moto, auto, camion]

for vehiculo in mis_vehiculos:
    vehiculo.mostrar_info()


# print(f"Tengo una moto {moto.marca} - {moto.modelo} en un estado {moto.estado} de color {moto.color}")

# print(f"Tengo un auto {auto.marca} - {auto.modelo} en un estado {auto.estado} de color {auto.color}")

# print(f"Tengo un camion {camion.marca} - {camion.modelo} en un estado {camion.estado} de color {camion.color}")
