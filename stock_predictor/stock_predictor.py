import numpy as np
import pandas as pd
import yfinance as yf

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from ta.momentum import RSIIndicator

STOCKS = ['WIPRO.NS', 'TCS.NS', 'INFY.NS']
PERIOD = '3y'
INTERVAL = '1d'
FIB_LOOKBACK = 60
RETURN_THRESHOLD = 0.02
PROB_THRESHOLD = 0.65

def add_fibonacci(df, lookback=60):
    high = df['High'].rolling(lookback).max()
    low = df['Low'].rolling(lookback).min()
    diff = high - low

    df['fib_382'] = high - 0.382 * diff
    df['fib_500'] = high - 0.500 * diff
    df['fib_618'] = high - 0.618 * diff

    close = df['Close'].squeeze()

    df['dist_fib_382'] = (close - df['fib_382'])/close
    df['dist_fib_500'] = (close - df['fib_500'])/close
    df['dist_fib_618'] = (close - df['fib_618'])/close

    return df

#Data Prepration

def prepare_data(symbol):
    df = yf.download(symbol, period= PERIOD, interval= INTERVAL, auto_adjust= False, progress= False)
    if df.empty or len(df) < 200:
        return None
    
    #force 1D series

    close = df['Close'].squeeze()
    volume = df['Volume'].squeeze()

    df['sma20'] = close.rolling(20).mean()
    df['sma50'] = close.rolling(50).mean()
    df['sma_ratio'] = df['sma20']/df['sma50']
    df['price_sma20'] = close / df['sma20']

    df['rsi'] = RSIIndicator(close, window=14).rsi()
    df['rsi_dist_50'] = df['rsi'] - 50
    df['rsi.slope'] = df['rsi'].diff()

    df['vol_sma20'] = volume.rolling(20).mean()
    df['vol_ratio'] = volume/df['vol_sma20']

    df = add_fibonacci(df, FIB_LOOKBACK)

    future_return = (close.shift(-5) - close)/close
    df['target'] = (future_return > RETURN_THRESHOLD).astype(int)
    df['symbol'] = symbol
    df.dropna(inplace=True)
    return df

FEATURES = [
    'rsi_dist_50',
    'rsi_slope',
    'sma_ratio',
    'price_sma20',
    'fib_dist_382',
    'fib_dist_500',
    'fib_dist_618',
    'vol_ratio'
]

print('\nDownloading and Preparing Data')

frames = []




