import pandas_datareader.data as web

import pandas as pd
 
import numpy as np
 
import datetime as dt
 
sdt = dt.datetime(2000, 1, 1)
 
edt = dt.datetime(2020, 1, 1)
 
cpi = web.DataReader("CPIAUCNS", "fred", sdt, edt)

cpi.head(n = 2)
'''
            CPIAUCNS
DATE
2000-01-01     168.8
2000-02-01     169.8
'''

df1 = pd.DataFrame({'month': [dt.datetime.strftime(i, "%Y-%m") for i in cpi.index]})
 
df1['qtr'] = [str(x.year) + "-Q" + str(x.quarter) for x in cpi.index]
 
df1['m_cpi'] = cpi.values
 
df1.index = cpi.index
 
grp = df1.groupby('qtr', as_index = False)
 
df2 = grp['m_cpi'].agg({'q_cpi': np.mean})
 
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'qtr', right_on = 'qtr')
 
df3['m_factor'] = np.array(df3.m_cpi)[-1] / df3.m_cpi
 
df3['q_factor'] = np.array(df3.q_cpi)[-1] / df3.q_cpi
 
df3.index = cpi.index
 
final = df3.sort_index(ascending = False)
 
final.head(12)
'''
              month      qtr    m_cpi       q_cpi  m_factor  q_factor
DATE
2020-01-01  2020-01  2020-Q1  257.971  257.971000  1.000000  1.000000
2019-12-01  2019-12  2019-Q4  256.974  257.176000  1.003880  1.003091
2019-11-01  2019-11  2019-Q4  257.208  257.176000  1.002966  1.003091
2019-10-01  2019-10  2019-Q4  257.346  257.176000  1.002429  1.003091
2019-09-01  2019-09  2019-Q3  256.759  256.629333  1.004720  1.005228
2019-08-01  2019-08  2019-Q3  256.558  256.629333  1.005508  1.005228
2019-07-01  2019-07  2019-Q3  256.571  256.629333  1.005457  1.005228
2019-06-01  2019-06  2019-Q2  256.143  255.927667  1.007137  1.007984
2019-05-01  2019-05  2019-Q2  256.092  255.927667  1.007337  1.007984
2019-04-01  2019-04  2019-Q2  255.548  255.927667  1.009482  1.007984
2019-03-01  2019-03  2019-Q1  254.202  252.896667  1.014827  1.020065
2019-02-01  2019-02  2019-Q1  252.776  252.896667  1.020552  1.020065
'''
