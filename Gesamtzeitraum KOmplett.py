import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

data = pd.read_csv('monthly.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

def lppl(t, tc, m, w, phi, A, B, C):
    time_to_tc = np.maximum(tc - t, 1e-3)
    return A + B * (time_to_tc ** m) * (1 + C * np.cos(w * np.log(time_to_tc) + phi))

def objective(params, t, prices):
    return np.sum((prices - lppl(t, *params)) ** 2)

params_initial = [1000, 0.5, 10, 3, np.mean(data['Price']), 100, 0.1]
bounds = [(500, 1500), (0, 1), (5, 15), (0, 2 * np.pi), (0, 2 * np.max(data['Price'])), (-np.max(data['Price']), np.max(data['Price'])), (-1, 1)]
result = minimize(objective, params_initial, args=(np.arange(len(data['Price'])), data['Price']), bounds=bounds)

if result.success:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Price'], label='Gold Preis')
    plt.plot(data.index, lppl(np.arange(len(data['Price'])), *result.x), label='LPPL Methode')
    plt.legend()
    plt.show()


def rolling_lppl_analysis(prices, window_size, step_size):
    results = []
    t = np.arange(window_size)

    for start in range(0, len(prices) - window_size + 1, step_size):
        window_prices = prices.iloc[start:start + window_size]
        params_initial = [window_size + 100, 0.5, 10, 3, np.mean(window_prices), 100, 0.1]
        bounds = [(window_size, 2 * window_size), (0, 1), (5, 15), (0, 2 * np.pi), (0, 2 * np.max(window_prices)),
                  (-np.max(window_prices), np.max(window_prices)), (-1, 1)]

        result = minimize(objective, params_initial, args=(t, window_prices), bounds=bounds)
        if result.success:
            temp_df = pd.DataFrame([{
                'Date': prices.index[start + window_size - 1],
                'tc': result.x[0],
                'm': result.x[1],
                'w': result.x[2],
                'phi': result.x[3],
                'A': result.x[4],
                'B': result.x[5],
                'C': result.x[6]
            }])
            results.append(temp_df)

    if results:
        return pd.concat(results, ignore_index=True)
    else:
        return pd.DataFrame()

lppl_results = rolling_lppl_analysis(data['Price'], window_size=252, step_size=20)
print(lppl_results)
lppl_results.to_excel('lppl_analysis_results.xlsx', index=False)
lppl_results.to_csv('lppl_analysis_results.csv', index=False)


