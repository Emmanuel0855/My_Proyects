#1. Importing Necessary Libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2. Loading and Exploring the Dataset:
# Load the dataset with a specified encoding (e.g., ISO-8859-1)
df = pd.read_csv(r'C:\Users\Zephyrus\Downloads\extended_car_models.csv', encoding='ISO-8859-1')

# Get basic information about the dataset
print(df.head())  # Display the first few rows
print(df.tail())  # Display the last few rows
print(df.info())  # Get information about data types and missing values
print(df.describe())  # Get summary statistics

#3. Handling Missing Values:
# Check for missing values
print(df.isnull().sum())  # Count missing values per column

# Handle missing values in the 'Modelo' column
df['Modelo'] = df['Modelo'].fillna(df['Modelo'].mode()[0])  # Fill with the most frequent value

#4. Data Cleaning and Transformation:
# Convert data types if necessary
df['Modelo del Motor'] = df['Modelo del Motor'].astype('category')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create new features or transform existing ones
# Ensure 'column1' and 'column2' exist before using them
if 'column1' in df.columns and 'column2' in df.columns:
    df['new_feature'] = df['column1'] / df['column2']
else:
    print("One or both columns 'column1' and 'column2' do not exist in the DataFrame.")

#5. Exploratory Data Analysis (EDA):
# Univariate analysis
sns.histplot(df['Cilindrada (L)'])  # Histogram
sns.boxplot(x=df['Cilindrada (L)'])  # Box plot
sns.countplot(x='categorical_column', data=df)  # Count plot

# Bivariate analysis
sns.scatterplot(x='column1', y='column2', data=df)  # Scatter plot
sns.barplot(x='categorical_column', y='numerical_column', data=df)  # Bar plot
sns.heatmap(df.corr())  # Correlation matrix