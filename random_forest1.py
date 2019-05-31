#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sb
from sklearn.ensemble import RandomForestClassifier


# In[11]:


#loading data
df=pd.read_csv('social.csv')


# In[12]:


# meta data of pandas
df.info()


# In[13]:


df['Age']


# In[14]:


# installing seaborn
get_ipython().system('sudo pip3 install seaborn')


# In[15]:


import seaborn as sb


# In[16]:


df.head()


# In[18]:


sb.countplot(df['Purchased'])


# In[19]:


# age count
sb.countplot(df['Age'])


# In[20]:


sb.countplot(df['Gender'])


# In[21]:


# features and labels
f=df.iloc[:,2:4].values
l=df.iloc[:,-1].values


# In[26]:


# training and testing
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(f,l,test_size=0.2,random_state=0)


# In[27]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()


# In[28]:


train_x=sc.fit_transform(train_x)


# In[31]:


test_x=sc.transform(test_x)


# In[32]:


# n_estimator=twenty trees  (by default 10 trees)
clf=RandomForestClassifier(n_estimators=20,criterion='entropy')


# In[33]:


trained=clf.fit(train_x,train_y)


# In[34]:


trained.predict(test_x)


# In[ ]:




