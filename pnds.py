#print hello world

import pandas as pd

pd.options.display.max_rows = 1 #(количество строк)

df = pd.read_csv('5.csv')

strr = df.to_string()

print(strr)

print(df.info())


#df1 = pd.read_csv('100.csv')

#strr = df1.to_string()

#print(strr)

df = pd.read_json('RRR.json')

strr = df.to_string()

print(strr)

#pd.options.display.max_rows = 1 #(количество строк)

#df = pd.read_csv('5.csv')

#print(df.head(3))

#pd.options.display.max_rows = 1 #(количество строк)

#df = pd.read_csv('5.csv')

#print(df.tail())

pd.options.display.max_rows = 1 #(количество строк)

df = pd.read_csv('5.csv')

