import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\Zephyrus\Documents\Random_num.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows and the structure of the dataset
data.head(), data.info()

# Flatten the data to a 1D array for easy frequency analysis
values = data.values.flatten()

# Define the intervals
bins = np.arange(0, 1, 0.1)
interval_labels = [f"{round(b, 1)}-{round(b + 0.1, 1)}" for b in bins[:-1]]

# Create the frequency table
frequency_counts = pd.cut(values, bins=bins, labels=interval_labels, include_lowest=True).value_counts().sort_index()

# Convert to DataFrame for a clear table view
frequency_table = pd.DataFrame({"Interval": interval_labels, "Frequency": frequency_counts.values})
frequency_table


# Calculate n (total number of data points)
n = values.size

# Display the frequency table
print("Frequency Table:")
print(frequency_table)
print(f"\nTotal data points (n): {n}\n")

# Plot the bar graph for interval frequencies
plt.bar(frequency_table['Interval'], frequency_table['Frequency'], color='skyblue', edgecolor='black')
plt.xlabel('Value Intervals')
plt.ylabel('Frequency')
plt.title('Frequency Distribution Across Intervals')
plt.xticks(rotation=45)
plt.show()

# Conclusion analysis
if frequency_table['Frequency'].nunique() == 1:
    conclusion = "The distribution appears uniform, suggesting independence."
else:
    conclusion = "The distribution shows variability, suggesting some intervals may have a higher frequency, indicating dependence."
    
print("Conclusion:")
print(conclusion)