#pandas series
import numpy as n
import pandas as p
import matplotlib as m
#Series
#ser=p.Series(n.array([1,2,3]))#using array
#ser=p.Series(n.array([1,2,3]),index=[11,22,33])#using array with index
#ser=p.Series([1,2,3],copy=False)#using list
#ser=p.Series((1,2,3))#using tuple
#ser=p.Series({"he":"she","me":"my","they":"them"})#using dictionary
#ser=p.Series(10,index=[x for x in range(10)])#by the scalar value
#ser=p.Series(n.linspace(1,100,10))
#print(ser)
'''
#DataFrame
#df=p.DataFrame([1,2,3,4,5,6,7],index=[x for x in range(7)])#using list
df=p.DataFrame([[1,2,3],[3,4],[5,6],[7,8]],columns=[x for x in range(3)])#using nexted list
#df=p.DataFrame({"name":["alan","turing","subu","srini"],"age":[10 for x in range(4)]})
print(df)
'''
d=p.read_csv("gapminder-FiveYearData.csv")
'''loc'''
# selecting rows with country 'Afghanistan' and year==1957
print(d.loc[(d.country=="Afghanistan")&(d.year==1957)])#using boolean condition locking
# selecting range of rows from 2 to 5
print(d.loc[2 : 5]));print(d.loc[2::5]);print(d.loc[2:55:4])
# updating values of country if Year < 2015
print(d.loc[(d.year < 2015), ['country']] = 'Afghanistan')
'''iloc'''
# selecting 0th, 2th, 4th, and 7th index rows
print(data.iloc[[0, 2, 4, 7]])
# selecting rows from 1 to 4 and columns from 2 to 4
display(data.iloc[1 : 5, 2 : 5])


