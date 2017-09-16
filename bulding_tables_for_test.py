
import pandas as pd
import numpy as np
import sqlite3
import datetime
import matplotlib.pyplot as plt

range = pd.date_range('2015-01-01', '2015-12-31', freq='D')
print(len(range))
df = pd.DataFrame(index = range)
df.reset_index(level=0, inplace=True)
df['Trans Date'] = df['index']
df.drop('index', axis=1, inplace=True)
df['Amount'] = np.random.randint(1,100, df.shape[0])
df['Category'] = 'none'
df['Category'].iloc[:55] = 'food' 
df['Category'].iloc[55:100] = 'gym' 
df['Category'].iloc[100:155] = 'mortgage' 
df['Category'].iloc[155:255] = 'supps' 
df['Category'].iloc[255:305] = 'social' 
df['Category'].iloc[305:] = 'misc' 
df['Type'] = 'Credit Card'
df['Post Date']= 'none'
df['Description'] = 'none'
df['Additional Info'] = 'none'
print(len(df))
print(df.head(10))
con = sqlite3.connect('/home/mike/Documents/coding_all/productivity_app/finance_db')
#df.to_sql('year_test_table1', con)
print(df['Category'].unique())