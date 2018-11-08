#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Practice 3-A

import requests

def converting_currencies (amount = 0, curr_from = '', curr_to = ''):

    link_fixer = 'http://data.fixer.io/api/latest'

    parameters = {
        "access_key" : "cad679e58b7d9088121c25f6c1e8542f",
    }
    response = requests.get(link_fixer,parameters).json()


    
    available_curr = response['rates']
    

    result = (response ['rates'][curr_from] / response ['rates'][curr_to]) * amount

    return (result, amount, curr_from, curr_to)


x = converting_currencies (amount = 1, curr_from = 'AFN', curr_to = 'AED')

print ('Base is: ', response['base'],'\n','Available Currencies with rates: ',
       response ['rates'], '\n') 


print ('The result is: ', x)


# In[ ]:




