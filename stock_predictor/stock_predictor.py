import numpy as np
import pandas as pd
import yfinance as yf

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ta.momentum import RSIIndicator

STOCKS = ['WIPRO.NS']
PERIOD = '3y'
INTERVAL = '1d'
FIB_LOOKBACK = 60

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
    df = yf.download(symbol, period= PERIOD, interval= INTERVAL, progress= False)
    if df.empty or len(df) < 200:
        return None, None, None
    
    #force 1D series

    close = df['Close'].squeeze()
    volume = df['Volume'].squeeze()

    df['sma20'] = close.rolling(20).mean()
    df['sma50'] = close.rolling(50).mean()

    df['rsi'] = RSIIndicator(close, window=14).rsi()

    df['vol_sma20'] = volume.rolling(20).mean()
    df['vol_ratio'] = volume/df['vol_sma20']

    df = add_fibonacci(df, FIB_LOOKBACK)

    df['target'] = np.where(close.shift(-5) > close, 1, 0)
    df.dropna(inplace= True)

    FEATURE = [
        'rsi',
        'sma20',
        'sma50',
        'dist_fib_382',
        'dist_fib_500',
        'dist_fib_618',
        'vol_ratio'
    ]

    X =df[FEATURE]
    y= df['target']

    return X, y, df

#model
model = RandomForestClassifier(
    n_estimators= 300,
    max_depth= 6,
    min_samples_leaf= 15,
    n_jobs= 1,
    random_state= 42
)

#run model

for stock in STOCKS:
    print(f'\nProcessing{stock}')
    X, y, df = prepare_data(stock)

    if X is None:
        print('Not enough data, Skipping')
        continue
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, shuffle= False)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f' accuracy: {acc:.2f}')

    latest_features = X.iloc[-1].values.reshape(1, -1)
    signal = model.predict(latest_features)[0]

    trend = 'UPTREND' if df['sma20'].iloc[-1] > df['sma50'].iloc[-1] else 'DOWNTREND'

    if signal == 1:
        print(f'Signal: Buy(Swing) | Trend: {trend}')
    
    else:
        print(f'Signal: No Buy/ No Sell | Trend: {trend}')



    
