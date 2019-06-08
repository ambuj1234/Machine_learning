#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.datasets import load_iris


# In[ ]:


iris=load_iris()
features=iris.data
label=iris.target


# In[ ]:


from sklearn.model_selection import train_test_split
train_ir,test_ir,train_lb,test_lb=train_test_split(features,label)


# In[ ]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# In[ ]:


clf=KNeighborsClassifier(n_neighbors=5) # this is by default also
clf1=DecisionTreeClassifier()  # decision tree algo


# In[ ]:





# In[4]:


knn_trained=clf.fit(train_ir,train_lb)# knn algo
dss_trained=clf1.fit(train_ir,train_lb) # decision tree algo


# In[3]:


predicted=knn_trained.predict(test_ir)# knn algo

predicted1=dss_trained.predict(test_ir)#decision tree algo
predicted


# In[26]:


# accuracy
from sklearn.metrics import accuracy_score
accuracy_score(test_lb,predicted)# knn algo
accuracy_score(test_lb,predicted1)# decision tree algo


# In[ ]:




