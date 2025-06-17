class Vehiculo():
    contador_vehiculo = 0


    def __init__(self, marca, modelo, estado):
        self.x = marca               #PUBLICO
        self.y = modelo              #PUBLICO
        self._estado = estado        #PROTEGIDO
        self.__id_vehiculo = Vehiculo.contador_vehiculo + 1    #PRIVADO

        Vehiculo.contador_vehiculo += 1

    def __str__(self):
        return f"Marca: {self.x}, Modelo: {self.y}, Estado: {self._estado}, ID: {self.__id_vehiculo}"
    #Si no esta este __str__ cuando haga print(auto) me va a dar el objeto y su ubicacion, en cambio ahora me lo va a salir asi como puse aca


    def mostrar_info(self):
        print(f"Marca: {self.x}\nModelo: {self.y}\nEstado: {self._estado}")

        
    def get_estado(self):
        return self._estado
    #Con este get puedo llamar a un privado o protegido para no llamarlo fuera de la clase
    

    def set_estado(self, nuevo_estado):
        self._estado = nuevo_estado


    def _realizar_inspeccion(self):     #PROTEGIDO
        print(f"Realizar inspeccion: {self.__id_vehiculo}")

    def __registrar_en_sistema(self):   #PRIVADO
        print(f"Realizando inspeccion del vehicuLo: {self.__id_vehiculo}")

    @classmethod           #Es una funcion que envuelve mi funcion
    def get_contador_vehiculo(cls):#No recibira self, si no la cls
        return cls.contador_vehiculo
    
    @staticmethod
    def clacular_costo_reparacion(hs_trabajo, tarifa_hs):
        return hs_trabajo * tarifa_hs

v = Vehiculo("Toyota", "Yaris", "Excelente")
print(v)
v2 = Vehiculo("Ford", "Ranger", "Bueno")
print(v2.get_contador_vehiculo())
print(Vehiculo.get_contador_vehiculo())

print(v2.clacular_costo_reparacion(3, 5000))


# v.mostrar_info()
# v._estado                         #INCORRECTO
# print(v.get_estado())             #CORRECTO
# print(v._Vehiculo__id_vehiculo)   #INCORRECTO
