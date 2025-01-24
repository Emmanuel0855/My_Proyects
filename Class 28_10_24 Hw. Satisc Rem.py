import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace this with your actual data set
data = [5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 10, 11, 13, 8, 5, 7, 9, 12, 13]

# Define intervals
intervals = [(5, 6), (7, 8), (9, 10), (11, 12), (13, 13)]

# Calculate absolute frequencies
frequency_abs = [sum(1 for x in data if interval[0] <= x <= interval[1]) for interval in intervals]

# Calculate relative frequencies
total_data = len(data)
frequency_rel = [f / total_data for f in frequency_abs]

# Calculate cumulative frequencies
cumulative_freq = np.cumsum(frequency_abs)

# Create a DataFrame to show the frequencies
df = pd.DataFrame({
    'Interval': [f"{interval[0]}-{interval[1]}" for interval in intervals],
    'Absolute Frequency (f)': frequency_abs,
    'Relative Frequency (fr)': frequency_rel,
    'Cumulative Frequency': cumulative_freq
})

print(df)

#Inciso A Plot the histogram
# Relative Frequency Histogram
plt.bar(df['Interval'], df['Relative Frequency (fr)'], color='skyblue', edgecolor='black')
plt.xlabel('Wind Speed Intervals (mph)')
plt.ylabel('Relative Frequency')
plt.title('Relative Frequency Histogram of Wind Speeds')
plt.xticks(rotation=45)
plt.show()

#Inciso C
# Count the number of data points exceeding Chicago's wind speed
count_exceeding_chicago = sum(1 for x in data if x > 10.4)
percentage_exceeding_chicago = (count_exceeding_chicago / total_data) * 100

print(f"Percentage of cities with average wind speeds exceeding 10.4 mph: {percentage_exceeding_chicago:.2f}%")