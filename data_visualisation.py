#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing matplotlib
import matplotlib.pyplot as plt

#importing matplotlib
import matplotlib.pyplot as plt
# In[4]:


x=range(10)


# In[5]:


x


# In[18]:


#we can create two list
x1=[2,6,8,9]
y1=[3,7,5,1]

x2=[12,26,18,19]
y2=[22,14,18,33]


# In[22]:


plt.xlabel("distance")
plt.ylabel("time")
plt.grid(c='green')  # to put graph grid
plt.plot(x1,y1,label="cars")
plt.plot(x2,y2,label="bikes")
plt.legend()  ## to show the label of plot


# ## bar plots
# 

# In[28]:


plt.xlabel('time')
plt.ylabel('price')
plt.bar(x1,y1,label='apple')
plt.bar(x2,y2,label='microsoft')
plt.plot(x1,y1,label='amazon',c='green')
plt.grid(c='red')
plt.legend()


# ## cricket score

# In[29]:


players=["virat","dhoni","sachin"]
runs=["234","435","987"]


# In[31]:


plt.bar(players,runs)
plt.xlabel("players")
plt.ylabel("run")
plt.grid(c='r')


# # scatter plot

# In[41]:


plt.scatter(x1,y1,marker='*',s=200)
plt.scatter(x2,y2,marker='^',s=200)
plt.plot(x1,y1)
plt.grid(c='y')


# In[42]:


import numpy as np


# In[43]:


x=np.array([3,6,8,11,12,22,24])


# In[44]:


x


# In[45]:


y=x**2


# In[46]:


y


# In[51]:


plt.scatter(x,y)
plt.bar(x,y)
plt.scatter(x,x**3,marker='*')


# In[ ]:




