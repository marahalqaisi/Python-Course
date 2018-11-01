#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Practice 2-D

states = ["Irbid", 'Ajloun', 'Jarash', 'Balqa\'a', 'Mafraq', 'Amman',
          'Zarqa', 'Madaba', 'Karak', 'Tafeelah','Ma\'an', 'Aqaba']

#Printing the cities with 5 letters only

for i in states:
    length =  len (i)
    if length == 5:
        print (i)
        


# In[7]:


for i in states: 
    if i == 'Ajloun' or i == 'Amman' or i == 'Aqaba':
        print (i)

