from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = get_history(symbol="TCS", start=date(2015, 1, 1), end=date(2016, 1, 31))

data_ts = pd.Series((data['Close']).rolling(window=10).mean(), name='time series data')
ts = data.join(data_ts)

plt.plot(ts['Close'])
plt.show()

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    # Plot rolling statistics:
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)


test_stationarity(ts['Close'])

ts_log = np.log(ts['Close'])

plt.plot(ts_log)
plt.show()
moving_avg = pd.rolling_mean(ts_log, 10)
plt.plot(ts_log)
plt.plot(moving_avg, color='red')
plt.show()

