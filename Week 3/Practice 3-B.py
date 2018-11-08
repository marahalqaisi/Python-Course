#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Practice 3-B


import requests
link = "http://api.openweathermap.org/data/2.5/weather"

lat = float (input ('Latitude= '))
lon = float (input ('Longitude= '))

additional_data = {
    "APPID" : "cae8c2fe3c590baaf937aefd3c4e59e2",
    "lat": lat,
    "lon": lon,
    "units" : "metric"
}

data = requests.get(link,params=additional_data).json()

print(data)

