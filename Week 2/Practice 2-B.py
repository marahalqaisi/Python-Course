#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Practice 2-B

currency1 = str (input ("What do you want to convert from? <JOD, TRY, USD>  "))
print ("\n")
currencya = float (input ("Please Enter the amount  "))
print ("\n")
currency2 = str (input ("What do you want to convert To? <JOD, TRY, USD>  "))
print ("\n")

if currency1 == 'JOD' and currency2 == 'TRY' :
    TRY = currencya * 7.76243
    print ("Note that: 1 JOD = 7.76243 TRY\n", "The result is: ", TRY, " TRY")
    
    
elif currency1 == 'JOD' and currency2 == 'USD' :
    USD = currencya * 1.4104
    print ("Note that: 1 JOD = 1.4104 USD\n", "The result is: ", USD, " USD")
    
    
elif currency1 == 'JOD' and currency2 == 'JOD' :
    print ("invalid inputs. Please try again.")

    
elif currency1 == 'TRY' and currency2 == 'JOD' :
    JOD = currencya/7.76243
    print ("Note that: 1 JOD = 7.76243 TRY\n", "The result is: ", JOD, " JOD")
    
    
elif currency1 == 'TRY' and currency2 == 'USD' :
    TRY = currencya * 0.18170
    print ("Note that: 1 TRY = 0.18170 USD\n", "The result is: ", USD, " USD")

    
elif currency1 == 'TRY' and currency2 == 'TRY' :
    print ("invalid inputs. Please try again.")
    
    
elif currency1 == 'USD' and currency2 == 'JOD' :
    JOD = currencya/1.4104
    print ("Note that: 1 JOD = 1.4104 USD\n", "The result is: ", USD, " USD")
    

elif currency1 == 'USD' and currency2 == 'TRY' :    
    TRY = currencya/0.18170
    print ("Note that: 1 TRY = 0.18170 USD\n", "The result is: ", TRY, " TRY")
    
elif currency1 == 'USD' and currency2 == 'USD' :
    print ("invalid inputs. Please try again.")


# In[ ]:




