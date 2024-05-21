import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression
plt.switch_backend('TkAgg')

file_path = 'monthly.csv'
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')
data = data.set_index('Date')
data = data.asfreq('MS')

data_1970_1980 = data['1970-01-01':'1980-12-31']
data_2008_2013 = data['2008-01-01':'2013-12-31']

model_1970_1980 = MarkovRegression(data_1970_1980['Price'], k_regimes=2, trend='c')
results_1970_1980 = model_1970_1980.fit()

model_2008_2013 = MarkovRegression(data_2008_2013['Price'], k_regimes=2, trend='c')
results_2008_2013 = model_2008_2013.fit()

fig, ax = plt.subplots(figsize=(12, 6))
data_1970_1980['Price'].plot(ax=ax, color='k', lw=1, label='Preis')
regime_1970_1980_0 = results_1970_1980.smoothed_marginal_probabilities[0]
regime_1970_1980_1 = results_1970_1980.smoothed_marginal_probabilities[1]

ax.fill_between(data_1970_1980.index, 0, 1, where=regime_1970_1980_0 > 0.5, color='green', alpha=0.2, transform=ax.get_xaxis_transform(), label='Wahrscheinlichkeit von Regime 0')
ax.fill_between(data_1970_1980.index, 0, 1, where=regime_1970_1980_1 > 0.5, color='yellow', alpha=0.2, transform=ax.get_xaxis_transform(), label='Wahrscheinlichkeit von Regime 1')

plt.xlabel('Datum')
plt.ylabel('Preis')
plt.title('Analyse des Zeitraum 1970-1980 mit Markov Regime Switching Model')
plt.legend()
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))
data_2008_2013['Price'].plot(ax=ax, color='k', lw=1, label='Preis')
regime_2008_2013_0 = results_2008_2013.smoothed_marginal_probabilities[0]
regime_2008_2013_1 = results_2008_2013.smoothed_marginal_probabilities[1]

ax.fill_between(data_2008_2013.index, 0, 1, where=regime_2008_2013_0 > 0.5, color='green', alpha=0.2, transform=ax.get_xaxis_transform(), label='Wahrscheinlichkeit von Regime 0')
ax.fill_between(data_2008_2013.index, 0, 1, where=regime_2008_2013_1 > 0.5, color='yellow', alpha=0.2, transform=ax.get_xaxis_transform(), label='Wahrscheinlichkeit von Regime 1')

plt.xlabel('Datum')
plt.ylabel('Preis')
plt.title('Analyse des Zeitraum 2008-2013 mit Markov Regime Switching Model)')
plt.legend()
plt.show()
