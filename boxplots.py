import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

annual_data = pd.read_csv(r'C:\Users\marti\PycharmProjects\Goldpreisprüfung\data\annual.csv')
annual_data['Date'] = pd.to_datetime(annual_data['Date'])

plt.figure(figsize=(7, 5))
plt.hist(annual_data['Price'], bins=20, color='gold', edgecolor='black')
plt.title('Verteilung der jährlichen Goldpreise')
plt.xlabel('Preis (USD)')
plt.ylabel('Häufigkeit')
plt.show()

plt.figure(figsize=(7, 5))
plt.boxplot(annual_data['Price'], vert=False, patch_artist=True)
plt.title('Boxplot der jährlichen Goldpreise')
plt.xlabel('Preis (USD)')
plt.show()
