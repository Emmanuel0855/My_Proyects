import csv

# Definir la clase Coche
class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}')

# Función para leer el archivo CSV usando el módulo csv
def leer_csv(file_path):
    datos = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lector_csv = csv.reader(file)
            next(lector_csv)  # Saltar la cabecera
            for fila in lector_csv:
                datos.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {file_path}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return datos

# Usar ruta corregida
file_path = "C:/Users/Zephyrus/Downloads/Car_Models.csv"
car_data = leer_csv(file_path)

# Crear dos objetos de la clase Coche usando datos de la base
if car_data:
    coche1 = Coche(marca=car_data[0][0], modelo=car_data[0][1], anio=car_data[0][9])
    coche2 = Coche(marca=car_data[1][0], modelo=car_data[1][1], anio=car_data[1][9])

    # Mostrar la información de cada coche
    coche1.mostrar_info()
    coche2.mostrar_info()
else:
    print("No se pudo cargar los datos del archivo CSV.")