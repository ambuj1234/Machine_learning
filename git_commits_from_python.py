#!/usr/bin/env python
# coding: utf-8

# In[41]:


from bs4 import BeautifulSoup as bs
import requests


# In[42]:


source=requests.get('https://github.com/vivek-git').text


# In[43]:


soup=bs(source,'html.parser')


# In[44]:


print(soup.prettify())


# In[47]:



for i in soup.find_all("rect",{'class':"day"}):
        print(i)
    
   


# In[ ]:




