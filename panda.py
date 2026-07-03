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


#DATAFRAME

# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

print(pd.DataFrame(student_data,columns=['iq','marks','package']))

# using dicts

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
print(students)

movis = pd.read_csv('./data/movies.csv')
ipl = pd.read_csv('./data/ipl-matches.csv')
print(movis)
print(movis.shape)#total rows and colmns
print(movis.columns)
print(movis.values)
print(movis.head())
print(movis.tail())
print(movis.sample())
print(movis.info())
print(movis.describe())
print(movis.isnull().sum())
print(movis.duplicated().sum())

#MATHEMATICAL FNS

print(students.sum(axis=1))  #row wise

print(students.sum()) #sums colmn wise

print(students.mean())
print(students.median())
print(students.std())
print(students.var())

#fetching

print(movis[['poster_path','runtime','genres']])


### Selecting rows from a DataFrame

# - **iloc** - searches using index positions
# - **loc** - searches using index labels 

print(movis.iloc[0])
print(movis.iloc[0:5])
print(movis.iloc[[0,4,5]])
print(movis.iloc[0:3,0:3])


print(students.loc['nitish'])

# print(ipl)

# print(ipl.loc['WinningTeam'])
print(ipl.loc[0:,'WinningTeam'])