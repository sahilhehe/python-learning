### What is Pandas

# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language.

# https://pandas.pydata.org/about/index.html


### Pandas Series

# A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.

import numpy as np
import pandas as pd


country =['INDIA','PAKISTAN','JAPAN']
print(pd.Series(country))

# custom index
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

print(pd.Series(marks,index=subjects))

marks = {
    'maths':67,
    'english':57,
    'science':57,
    'hindi':100
}

marks_series = pd.Series(marks,name='sahil ke marks')
print(marks_series)

print(marks_series.size)
print(marks_series.dtype)
print(marks_series.name)
print(marks_series.is_unique)  #true if marks are diff
print(marks_series.index)
print(marks_series.values)

subs= pd.read_csv('./data/subs.csv').squeeze("columns")
rn= pd.read_csv('./data/kohli_ipl.csv',index_col='match_no').squeeze("columns")
mov= pd.read_csv('./data/bollywood.csv',index_col='movie').squeeze("columns")
# print(subs)
# print(rn)
# print(type(rn))
# print(rn.head()) top 5
# print(rn.tail()) last 5
# print(rn.sample()) random 


print(mov) 
print(mov.value_counts())  #frequency of values

print(rn.sort_values(ascending=False).head(1).values[0])  #highest run by virat kuli, eg of method chaining, sort by values

print(mov.sort_index())  #sort by index

print(rn.count())
print(subs.sum())  #sum of values


#statistical data
print(subs.mean())
print(rn.mean())
print(rn.median())

print(mov.mode())

print(subs.min())
print(subs.max())


print(rn.describe())  #importan, gives u everything

# for values in mov:
#     print(values)

print(rn[rn==0].size)