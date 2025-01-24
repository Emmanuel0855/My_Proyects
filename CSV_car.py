import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Cargar el dataset
df = pd.read_csv('C:/Users/Zephyrus/Downloads/car_models(1).csv')

# Información básica del dataset
print(df.head())  
print(df.tail())  
print(df.info())  
print(df.describe())  

# Manejo de valores nulos
print(df.isnull().sum())  

# Rellenar valores nulos en 'Modelo' con el valor más frecuente
df['Modelo'].fillna(df['Modelo'].mode()[0], inplace=True)

# O eliminar filas con valores nulos
# df.dropna(inplace=True)

# Transformación y limpieza de datos
df['Modelo del Motor'] = df['Modelo del Motor'].astype('category')
df.drop_duplicates(inplace=True)
df['Promedio de precios (USD)'] = df['Precio Actual de Mercado (USD)'] / df['Precio de Lanzamiento (USD)']

# Análisis exploratorio de datos (EDA)
sns.histplot(df['Precio Actual de Mercado (USD)'])  
plt.show()

sns.boxplot(x=df['Precio de Lanzamiento (USD)'])  
plt.show()

sns.countplot(x='Categoría', data=df)  
plt.show()

sns.scatterplot(x='Año de Lanzamiento', y='Precio Actual de Mercado (USD)', data=df)  
plt.show()

sns.barplot(x='Categoría', y='Cilindros', data=df)  
plt.show()

sns.heatmap(df.corr(numeric_only=True))  
plt.show()