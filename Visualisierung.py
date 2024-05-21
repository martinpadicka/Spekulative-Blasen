import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = pd.read_csv('lppl_analysis_results.csv')
data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(15, 10))

plt.subplot(7, 1, 1)
plt.plot(data['Date'], data['tc'], label='Critical Time (tc)', marker='o')
plt.title('Kritische Zeit (tc) im Zeitverlauf')
plt.ylabel('tc')

plt.subplot(7, 1, 2)
plt.plot(data['Date'], data['m'], label='Exponent (m)', marker='o', color='red')
plt.title('Exponent (m) im Zeitverlauf')
plt.ylabel('m')

plt.subplot(7, 1, 3)
plt.plot(data['Date'], data['w'], label='Frequenz (w)', marker='o', color='green')
plt.title('Frequenz (w) im Zeitverlauf')
plt.ylabel('w')

plt.subplot(7, 1, 4)
plt.plot(data['Date'], data['phi'], label='Frequenz (phi)', marker='o', color='green')
plt.title('Frequenz (phi) im Zeitverlauf')
plt.ylabel('phi')

plt.subplot(7, 1, 5)
plt.plot(data['Date'], data['A'], label='Frequenz (A)', marker='o', color='green')
plt.title('Frequenz (A) im Zeitverlauf')
plt.ylabel('A')

plt.subplot(7, 1, 6)
plt.plot(data['Date'], data['B'], label='Frequenz (B)', marker='o', color='green')
plt.title('Frequenz (B) im Zeitverlauf')
plt.ylabel('B')

plt.subplot(7, 1, 7)
plt.plot(data['Date'], data['C'], label='Frequenz (C)', marker='o', color='green')
plt.title('Frequenz (C) im Zeitverlauf')
plt.ylabel('C')

plt.tight_layout()
plt.show()