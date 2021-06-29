import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", count=30)
df['range'] = (df['high'] - df['low']) * 0.6
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
print(df)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")
