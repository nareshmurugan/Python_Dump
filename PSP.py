#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import pandas_datareader as web
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')


# In[23]:


df = web.DataReader('AMZN',data_source= 'yahoo',start='2019-01-01',end='2022-12-01')
df


# In[24]:


#GEt the number of trading  days
df.shape


# In[25]:


#Visualize the cpd
plt.figure(figsize=(16,8))
plt.title('Stock Price Analysis',fontsize=30)
plt.xlabel('Close Price USD ($)',fontsize=25)
plt.ylabel('Days',fontsize=25)
plt.plot(df['Close'])
plt.legend(['Original Analysis till Date'],fontsize=20)
plt.show()


# In[26]:


#Get the close price
df=df[['Close']]
df.head(4)


# In[27]:


#Create the variable to predict 'x' days out into the future
future_days=60
#Create a new column (target )shifted 'x' units/days up
df['Prediction']=df[['Close']].shift(-future_days)
df.head(4)


# In[28]:


#Create the feature dataset (X) and convert into numpy
X=np.array(df.drop(['Prediction'], 1))[:-future_days]
#df.columns = df.columns.droplevel(1)
print(X)


# In[29]:


#CReate the target data as y and convert in2 numpy array  and get all oftarget values  except the  last X rows
y=np.array(df['Prediction'])[:-future_days]
print(y)


# In[30]:


#Split the dataa  in2 75% and 25%  testing
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25)


# In[31]:


#Create the models 
#Create thethe decision tree regressoor model
tree=DecisionTreeRegressor().fit(x_train,y_train)
#CReate  linear  regression model
lr=LinearRegression().fit(x_train,y_train)


# In[32]:


x_future=df.drop(['Prediction'], 1)[:-future_days]
x_future=x_future.tail(future_days)
x_future=np.array(x_future)
x_future


# In[33]:


#Show the model tree prediction
tree_prediction = tree.predict(x_future)
print(tree_prediction)
print()
#Show the modell lineaar regression prediction
lr_prediction=lr.predict(x_future)
print(lr_prediction)


# In[34]:


#Visualize the data using Tree
'''predictions=tree_prediction
valid=df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(18,9))
plt.title('Model',fontsize=30)
plt.xlabel('Days',fontsize=25)
plt.ylabel('Close Price USD ($)',fontsize=25)
plt.plot(df['Close'])
plt.plot(valid[['Close','Prediction']])
plt.legend(['Original','Value','Predict'],fontsize=20)
plt.show()
'''

# In[35]:


#Visualize the data using Linear
predictions=lr_prediction
valid=df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(18,9))
plt.title('Model',fontsize=30)
plt.xlabel('Days',fontsize=25)
plt.ylabel('Close Price USD ($)',fontsize=25)
plt.plot(df['Close'])
plt.plot(valid[['Close','Prediction']])
plt.legend(['Original','Value','Predict'])
plt.show()


# In[ ]:




