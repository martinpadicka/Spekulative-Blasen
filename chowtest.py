import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'monthly.csv'  

data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

column_name = 'Price'  

sns.lineplot(data=data, x=data.index, y=column_name)
plt.title('Goldpreis')
plt.xlabel('Jahr')
plt.ylabel('Preis in USD')
plt.show()
