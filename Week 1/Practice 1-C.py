#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Practice 1-C

#This code will convert temperatures from Celsius to Fahrenheit and vice versa
#The reference for the used converting equations is:
#http://allmeasures.com/temperature.html

in_temp = str (input ("What do you want to convert to? <F or C>  "))
print ("\n")

if in_temp == "F":
    print ("You want to convert from C to F")
    print ("\n")
    in_c = float (input("Enter the temperature in Celsius "))
    print ("\n")
    print ("The temperature you entered is ", in_c, "C")
    result = 32 + in_c*9/5
    print ("\n")
    print ("The converted temperature in F is: ", result, "F")
elif in_temp == "C":
    print ("You want to convert from F to C")
    print ("\n")
    in_f = float (input("Enter the temperature in Fahrenheit "))
    print ("\n")
    print ("The temperature you entered is ", in_f, "F")
    result1 = (5/9)*(in_f-32)
    print ("\n")
    print ("The converted temperature in C is: ", result1, "C")
else:
    print ("Your input is invalid")

