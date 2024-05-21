import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
monthly = pd.read_csv('monthly.csv')
monthly['Date'] = pd.to_datetime(monthly['Date'])

breakpoint = 2012
monthly['Post_2012'] = (monthly['Date'].dt.year > breakpoint).astype(int)

model = ols('Price ~ Date + Post_2012', data=monthly).fit()
print(model.summary())

pre_2012 = monthly[monthly['Date'].dt.year <= breakpoint]
post_2012 = monthly[monthly['Date'].dt.year > breakpoint]
f_val, p_val, _ = model.compare_f_test(ols('Price ~ Date', data=pre_2012).fit())
print("Chow Test p-value:", p_val)
