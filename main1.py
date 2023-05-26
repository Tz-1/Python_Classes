from clases import *

instance = []

n = int(input("Cuantos vehiculos desea insertar: "))

for i in range(n):
    while True:
        try:
            print(f"Datos del automovil {i+1}: ")
            marca =  input("Inserte la marca del automovil: ")
            modelo = input("Inserte el modelo: ")
            num_ruedas = int(input("Inserte el numero de ruedas: "))
            velocidad = int(input("Inserte la velocidad en km/h: "))
            cilindrada = int(input("Inserte el cilindraje en cc: "))
        except:
            print("\nDebe ingresar un numero. Intentelo de nuevo")
        else:
            print("")
            auto = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
            instance.append(auto)
            break

print("Imprimiendo por pantalla los Vehiculos: ")

for index,item in enumerate(instance):
    print(f"Datos del automovil {index + 1} : Marca: {item.marca}, Modelo: {item.modelo}, {item.num_ruedas} ruedas, {item.velocidad} Km/h, {item.cilindrada} cc")

