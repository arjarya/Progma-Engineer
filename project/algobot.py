import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= yf.download("RELIANCE.NS", period="6mo", interval="1d")

#Step 2: Prepare Data Columns
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [col[0] for col in data.columns]

#Step 3: Convert Data to Numeric Format
for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
    if col in data.columns:
        data[col]= pd.to_numeric(data[col], errors= 'coerce').astype(float)

print(data)