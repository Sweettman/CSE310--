import pandas as pds
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime as dt
plt.style.use('ggplot')

msft = yf.Ticker('googl')
stockinfo = msft.info

for key,value in stockinfo.items():
          print(key,":", value)
