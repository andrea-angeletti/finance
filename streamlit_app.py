# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import numpy as np

#plot = st.line_chart(np.random.randn(10, 2))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:40:51 2022

@author: a
"""
import time
start_time = time.time()
import yfinance as yf

from datetime import datetime, timedelta
#d = datetime.today() - timedelta(days=34)
#"2022-10-01"
#data = yf.download("AAPL", start=d, end=datetime.today())


from datetime import datetime, timedelta

now = datetime.now()
today=now.strftime('%Y-%m-%d')

period=14

before=now-timedelta(period+95)

then=before.strftime('%Y-%m-%d')

#df = yf.download("AAPL", start=then, end=today,interval="1d")
  

def rsi(df, periods = 14):
    """
    Returns a pd.Series with the relative strength index.
    """
    close_delta = df['Close'].diff()

    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    # Use exponential moving average
    ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
 
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    return rsi

#"^STOXX50","^IPSA","^TA125.T",

def notify (lista):
    promising=[]
    for i in lista:
        data = yf.download(i, start=then, end=today)
        a=rsi(data)
        if a[-1]>67 or a[-1]<33:
            #print(i)
            #print(a[-1])
            promising.append(i)
            promising.append(a[-1])
    for i in promising:
        print(i)      
        
def test ():
   
  
        data = yf.download("AAPL", start=then, end=today)
        a=rsi(data)
        print(a[-1])

test()

indexes=[
"^NYA",
"^XAX",
"^BUK100P",
"^RUT",
"^VIX",
"^FTSE",
"^GDAXI",
"^FCHI",

"^N100",
"^BFX",
"IMOEX.ME",
"^N225",
"^HSI",
"000001.SS",
"399001.SZ",
#"^STI",
"^AXJO",
"^AORD",
"^BSESN",
#"^JKSE",
"^KLSE",
"^NZ50",
"^KS11",
#"^TWII",
"^GSPTSE",
"^BVSP",
#"^MXX",
#"^MERV",

#"^CASE30",
#"^JN0U.JO"
]

currencies = [
"EURUSD=X",
"JPY=X",
"GBPUSD=X",
"AUDUSD=X",
"NZDUSD=X",
"EURJPY=X",
"GBPJPY=X",
"EURGBP=X",
"EURCAD=X",
"EURSEK=X",
"EURCHF=X",
"EURHUF=X",
"EURJPY=X",
"CNY=X",
"HKD=X",
"SGD=X",
"INR=X",
"MXN=X",
#"PHP=X",
"IDR=X",
#"THB=X",
#"MYR=X",
"ZAR=X",
"RUB=X",
"CADJPY=X",
"CADCHF=X"
]


commodities = [
"ES=F",
#"YM=F",
"NQ=F",
"RTY=F",
"ZB=F",
"ZN=F",
"ZF=F",
"ZT=F",
"GC=F",
"MGC=F",
"SI=F",
"SIL=F",
"PL=F",
"HG=F",
"PA=F",
"CL=F",
"HO=F",
"NG=F",
"RB=F",
"BZ=F",
"B0=F",
"ZC=F",
"ZO=F",
"KE=F", #wheat
#"ZR=F",
"ZM=F",
#"ZL=F", soybeans oil future
"ZS=F",
"GF=F",
"HE=F",
"LE=F",
"CC=F",
"KC=F",
"CT=F",
"LBS=F",
"OJ=F",
"SB=F",
]

lista=indexes+currencies+commodities


notify(lista)



print("--- %s seconds ---" % (time.time() - start_time))

'''
number=len(lista)

#for i in range(0,number-1):
#    if 
    
#print(rsi(data))
 
average_loss=1
average
RS=average_loss/average_gain​

RSI=100−1001+RS
RSI=100−1+RS100                                                                                                                                 
'''                                                                                          