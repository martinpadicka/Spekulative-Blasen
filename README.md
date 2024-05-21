# Spekulative-Blasen

In diesem Repository sind alle Codes enthalten, welche ich in der Arbeit genutzt habe. 

Darstellung 

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you're running this script in the same directory as your dataset
file_path = 'monthly.csv'  # Use the relative path to the CSV file

# Load the dataset from a local file
data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# Adjust the column name 'price' to match your dataset if it's different
column_name = 'Price'  # Replace 'price' with the correct column name from your CSV

# Visualization of Gold Prices
sns.lineplot(data=data, x=data.index, y=column_name)
plt.title('Goldpreis')
plt.xlabel('Jahr')
plt.ylabel('Preis in USD')
plt.show()



