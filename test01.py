import sys
sys.path.append(r'C:\Users\pc\Desktop\stock\Py_for_Finance\tool')
import pandas as pd
from tool import BSM

file = 'STOXX 50 Volatility VSTOXX EUR.csv'
path = 'C:/Users/pc/Desktop/stock/Py_for_Finance/data/'
df = pd.read_csv(path + file, index_col= 'Date')
#print(df.head())

