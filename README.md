# Vehicle Management System

## Description
This project implements a vehicle management system using Python object-oriented programming (OOP). It defines different types of vehicles such as cars, bicycles, and motorcycles, allowing the user to create instances, store them in a CSV file, and retrieve the stored data.

## Features
- Define various vehicle types using inheritance.
- Save vehicle data to a CSV file.
- Read and display stored vehicle data.
- Use `isinstance()` to check class relationships.

## Project Structure
```
/VehicleManagement
│── clases.py        # Defines vehicle classes and CSV handling functions
│── main1.py         # Allows the user to input vehicle data manually
│── main2.py         # Creates predefined vehicle instances and checks class relationships
│── main3.py         # Saves vehicle instances to CSV and retrieves stored data
│── Vehiculos.csv    # CSV file to store vehicle data (created automatically)
```

## Requirements
- Python 3.x

## How to Run
1. Clone this repository or download the files.
2. Open a terminal in the project directory.
3. Run one of the main scripts:
   - `python main1.py` to manually input vehicle data.
   - `python main2.py` to create and check predefined vehicles.
   - `python main3.py` to save and retrieve vehicle data.

## Class Overview
### `Vehiculo`
- Base class for all vehicles.
- Attributes: `marca`, `modelo`, `num_ruedas`.
- Methods: `guardar_datos_csv()`, `leer_datos_csv()`.

### `Automovil` (inherits from `Vehiculo`)
- Attributes: `velocidad`, `cilindrada`.

### `Particular` (inherits from `Automovil`)
- Additional attribute: `num_puesto`.

### `Carga` (inherits from `Automovil`)
- Additional attribute: `carga`.

### `Bicicleta` (inherits from `Vehiculo`)
- Additional attribute: `tipo_bici`.

### `Motocicleta` (inherits from `Bicicleta`)
- Additional attributes: `motor`, `cuadro`, `num_radios`.

## Example Output
```
How many vehicles do you want to insert? 2
Enter data for vehicle 1:
Brand: Toyota
Model: Corolla
Number of wheels: 4
Speed: 180 km/h
Cylindrical capacity: 1600 cc

Displaying stored vehicles:
Vehicle 1: Toyota Corolla, 4 wheels, 180 km/h, 1600 cc
```

## Notes
- The CSV file is automatically created when `guardar_datos_csv()` is called.
- Ensure `Vehiculos.csv` exists in the same directory as the scripts when running `leer_datos_csv()`.


