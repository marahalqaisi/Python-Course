#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Practice 1-B

import math
pi= math.pi

x = float (input ("Enter any number: "))

print ("\n")
print ("The number you entered is: ", x)

if x < -100:
    
    x = -1*x
    
elif x >= -100 and x <= -25:
    
    x = x**4
        
elif x > -25 and x <= 0:

    x = 3*(x**2)-1
    
elif x > 0 and x <= 100:
    
    x = x*(pi/2) + 3**x
    
print ("\n")
print ("The result is ", x)
    

