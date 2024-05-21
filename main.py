import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

file_path = 'monthly.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

def lppl(t, tc, m, w, phi, A, B, C):
    epsilon = 0.01
    adjusted_time = np.maximum(tc - t, epsilon)

    return A + B * (adjusted_time ** m) * (1 + C * np.cos(w * np.log(adjusted_time) + phi))

time_windows = {
    '1979-1980': ('1979-01-01', '1980-12-31'),
    '2008': ('2008-01-01', '2008-12-31'),
    '2011': ('2011-01-01', '2011-12-31')
}
data_windows = {key: data.loc[start:end] for key, (start, end) in time_windows.items()}

def fit_lppl(data, start_date, end_date):
    window_data = data.loc[start_date:end_date]
    prices = window_data['Price']
    t = np.arange(len(prices))
    params_initial = [max(t) + 100, 0.5, 7.0, 2.0, np.mean(prices), -100, 10]

    def objective(params):
        fit = lppl(t, *params)
        residuals = prices - fit
        return np.sum(residuals ** 2)

    result = minimize(objective, params_initial, method='L-BFGS-B')
    return result

    params_initial = [max(t) + 50, 0.5, 10, 2 * np.pi, np.mean(prices), -np.mean(prices), 0]
    bounds = [(max(t), 2 * max(t)), (0.1, 0.9), (5, 15), (0, 2 * np.pi), (0, 2 * np.max(prices)),
              (-2 * np.max(prices), 0), (-10, 10)]
    result = minimize(objective, params_initial, bounds=bounds, method='L-BFGS-B')

    def objective(params):
        try:
            fit = lppl(t, *params)
            residuals = prices - fit
            if np.any(np.isnan(residuals)):
                return np.inf
            return np.sum(residuals ** 2)
        except Exception as e:
            print(f"Error during optimization: {e}")
            return np.inf

    results = {window: fit_lppl(data, *time_windows[window]) for window in time_windows}
    return result

results = {window: fit_lppl(data, *time_windows[window]) for window in time_windows}

def plot_results(window):
    result = results[window]  # Hier erhalten Sie das Optimierungsergebnis direkt
    prices = data_windows[window]['Price']
    t = np.arange(len(prices))
    fitted_prices = lppl(t, *result.x)  # Korrekter Zugriff auf die optimierten Parameter

    plt.figure(figsize=(10, 5))
    plt.plot(prices.index, prices, label='Wert von Gold')
    plt.plot(prices.index, fitted_prices, label='LPPL Methode', linestyle='--')
    plt.title(f'LPPL Methode für den Zeitpunkt {window}')
    plt.xlabel('Jahr')
    plt.ylabel('Preis')
    plt.legend()
    plt.show()

for window in time_windows:
    plot_results(window)