import pandas as pd

# Ruta del archivo .xlsx
file_path = 'C:/Code_DataPre/cilindrada_vehiculos.xlsx'

# Leer el archivo Excel
df = pd.read_excel(file_path)

# Mostrar los datos del archivo
print(df)