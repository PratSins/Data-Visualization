'''
To know more about Plotly and cufflinks
    https://www.kaggle.com/code/vvineeth/plotly-cufflinks-and-iplot
'''

import pandas as pd
import numpy as np

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__) # requires version >= 1.9.0

import cufflinks as cf
#cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2.head())

print('Scatter')
# pip install chart_studio
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)