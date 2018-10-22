#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Practice 1-A

name =  str (input ("Enter your name: "))
num1 = float (input ("Enter the 1st number: "))
num2 = float (input ("Enter the 2nd number: "))


add = float (num1 + num2)
sub = float (num1 - num2)
multi = float (num1 * num2)
div = float (num1 / num2)
reminder = int (num1 % num2)
exp = float (num1 ** num2)
print ("\n")

print (f"Hello {name}!")
print ("\n")

print ("The summation of ", num1 ," and", num2 , "equals  ", add )
print ("\n")

print ("The subtraction of ", num1 ," and", num2 ,"equals  " , sub )
print ("\n")

print ("The multiplication of ", num1 , " and", num2 , "equals  " , multi )
print ("\n")

print ("The division of ", num1, " over", num2 , "equals  " , div  )
print ("\n")

print ("The reminder of  division of ", num1, " over", num2 , "equals  " , reminder )
print ("\n")

print ("The value of ", num1, " rasied to the power of ", num2 , " equals  " , exp )
print ("\n")


# In[ ]:




