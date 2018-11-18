from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
data =get_history(TCS="INFY",start=date(2015,1,1),end=date(2016,1,31))

def moving_average(wk):
    ndays =wk*7
    MA =pd.Series((data['Close']).rolling(window=ndays).mean(),name='wk'+'week moving average')
    return data.join(MA)
    
moving_average(4)
