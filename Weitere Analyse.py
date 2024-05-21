import pandas as pd
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

file_path = 'monthly.csv' 
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')
data = data.set_index('Date')
data = data.asfreq('MS')

data.rename(columns={'Price': 'Preis'}, inplace=True)

model = MarkovRegression(data['Preis'], k_regimes=2, trend='c')
results = model.fit()

smoothed_probs = results.smoothed_marginal_probabilities
regime = smoothed_probs.idxmax(axis=1)

results_df = data.copy()
results_df['Regime'] = regime
results_df['Wahrschein_Regime_0'] = smoothed_probs[0]
results_df['Wahrschein_Regime_1'] = smoothed_probs[1]

summary_stats = results_df.describe()

regime_durations = results_df['Regime'].groupby((results_df['Regime'] != results_df['Regime'].shift()).cumsum()).transform('size')
regime_frequency = results_df['Regime'].value_counts()

transition_matrix = results.filtered_marginal_probabilities.mean(axis=0)

results_df['Regime_Duration'] = regime_durations

print("Analyse:")
print(summary_stats)
print("\nRegime-Häufigkeit:")
print(regime_frequency)
print("\nWahrscheinlichkeit des Wechsels:")
print(transition_matrix)

results_df.to_csv('regime_switching_results.csv')
