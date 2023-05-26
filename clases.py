import csv

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def guardar_datos_csv(self):
        try:
            with open("Vehiculos.csv","a", newline="") as archivo:
                datos = [self.__class__, self.__dict__]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow(datos)

        except FileNotFoundError:
            print("No se encuentra el archivo")
        except Exception as error:
                print("Se ha generado un error no pevisto", type(error).__name__)
   
    def leer_datos_csv(self):
        try:
            with open("Vehiculos.csv","r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de vehiculos {type(self).__name__}: ")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                print("")

        except FileNotFoundError:
            print("No se encuentra el archivo")
        except Exception as error:
                print("Se ha generado un error no pevisto", type(error).__name__)


    def __str__(self):
        return f'\nMarca: {self.marca} \nModelo: {self.modelo}\n{self.num_ruedas} ruedas'

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f'\n{self.velocidad} Km/h \n{self.cilindrada} cc'

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puesto):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puesto = num_puesto

    def get_num_puesto(self):
        return self.num_puesto
    
    def set_num_puesto(self,num_puesto_new):
        self.num_puesto = num_puesto_new

    def __str__(self):
        return super().__str__() + f'\nPuestos: {self.num_puesto}'

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f'\nCarga: {self.carga}'

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo_bici):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bici = tipo_bici

    def __str__(self):
        return super().__str__() + f'\nTipo: {self.tipo_bici}'
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bici, motor, cuadro, num_radios):
        super().__init__(marca, modelo, num_ruedas, tipo_bici)
        self.num_radios = num_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return super().__str__() + f'\nMotor: {self.motor} \nCuadro: {self.cuadro} \nNro Radios: {self.num_radios}'