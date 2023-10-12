import pandas as pd
import quandl
df=quandl.get('WIKI/GOOGL')
df=df[['Adj. open','Adj. high','Adj. low','Adj. close','Adj. volume',]]
df['HL_PCT']=(df['Adj. high'] - df['Adj. open']) / df['Adj. close']*100.0
df['PCT_change']=(df['Adj. close'] - df['Adj. open']) / df['Adj. open']*100.0
df=df[['Adj. close','HL_PCT','PCT_change','Adj. volume']]
print(df.head())



    
