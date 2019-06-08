#!/usr/bin/env python
# coding: utf-8

# In[11]:


# assume some facts or data with features about apple and orange 0=smooth 1=bumpy
           # weight,texture
features=[[120,0],[130,0],[140,0],[145,1],[150,1],[160,1]]


# In[12]:


# labels or  answers
label=['apple','apple','apple','orange','orange','orange',]


# In[10]:


get_ipython().system('sudo pip3  install sklearn')


# In[3]:


get_ipython().system('sudo pip3 install --upgrade sklearn')


# In[4]:


# let's call any of the classifier decision
from sklearn import tree


# In[5]:


#let's explore
dir(tree)


# In[13]:


# creating decision tree classifier
clf=tree.DecisionTreeClassifier()


# In[15]:


# time for allocating data to classifier -- for training decision tree
trained=clf.fit(features,label)
    #      q     a


# In[44]:


# ask questions
output=trained.predict([[160,1],[100,0]])
print(output)


# In[ ]:





# In[ ]:




