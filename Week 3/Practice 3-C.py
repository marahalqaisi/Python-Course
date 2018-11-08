#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Practice 3-C

import os

x = os.listdir ()
print ('The files in the current directory are: ',x)


# In[ ]:


# Renaming

for i in x:
    y = 1+y
    name = 'File' + str (y)
    os.rename (i, name)

