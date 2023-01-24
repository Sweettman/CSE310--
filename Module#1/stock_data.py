import pandas as pds
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime as dt
plt.style.use('ggplot')

#By using these libraries I am able to obtain data on any 
#ticker symbol, and all the information that I could need
msft = yf.Ticker('googl')
stockinfo = msft.info

for key,value in stockinfo.items():
          print(key,":", value)
