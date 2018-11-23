#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#World Population
#List of available countries
#http://api.population.io/#!/wp-rank/worldPopulationRankToday

import requests

link = "http://api.population.io:80/1.0/countries"

countries = requests.get(link).json()

print ("This code will display world population for any country of interest ")
print ('\n')
print(countries)

country = str (input ('Please Choose a country of interest:  '))



# In[ ]:


#Ranking
#Calculates the world population rank of a person with the given date of birth, sex and country of origin as of today.
#The world population rank is defined as the position of someone's birthday among the group of living people of the same sex and country of origin, ordered by date of birth decreasing. The last person born is assigned rank #1.


import requests

dob = str ( input ('Date of birth (YYYY-MM-DD): '))
gender = str(input('Gender (female or male): '))

link = "http://api.population.io:80/1.0/wp-rank/"+dob+'/'+gender+'/'+country+'/'+'today/'

WorldPopulationRankToday = requests.get(link).json()

print ('Rank today is',WorldPopulationRankToday['rank'])


# In[ ]:


#Ranking
#Calculates the world population rank of a person with the given date of birth, sex and country of origin on a certain date.


import requests

dob = str ( input ('Date of birth (YYYY-MM-DD): '))
gender = str(input('Gender (female or male): '))
date = str ( input ('Date (YYYY-MM-DD): '))

link = 'http://api.population.io:80/1.0/wp-rank/'+dob+'/'+gender+'/'+country+'/'+'on'+'/'+date+'/'

WorldPopulationRank = requests.get(link).json()

print ('Rank is',WorldPopulationRank['rank'])


# In[ ]:


#Life Expectancy
#Calculate total life expectancy of a person with given sex, country, and date of birth.


import requests

dob = str ( input ('Date of birth (YYYY-MM-DD): '))
gender = str(input('Gender (female or male): '))


link = 'http://api.population.io:80/1.0/life-expectancy/total/'+gender+'/'+country+'/'+dob+'/'

LifeExoectancy = requests.get(link).json()

print ('Life Expectancy = ',LifeExoectancy ['total_life_expectancy'], ' years')


# In[ ]:


#Population Table
#Retrieve population table for a specific age group in the given year and country.


import requests

year = str (input ('Year of interest: '))
age = str ( input ('age = '))

link = 'http://api.population.io:80/1.0/population/'+year+'/'+country+'/'+age+'/'

PopulationTable = requests.get(link).json()

print (' Age = ',PopulationTable[0]['age'],'\n', 'Males: ', PopulationTable[0]['males'], '\n','Females: ', PopulationTable[0]['females'])


# In[ ]:


#Population today and tomorrow
#Determines total population for a given country with separate results for today and tomorrow.


import requests

link = 'http://api.population.io:80/1.0/population/'+country+'/today-and-tomorrow/'

PopulationTodayAndTomorrow = requests.get(link).json()

print (PopulationTodayAndTomorrow['total_population'][0], '\n', PopulationTodayAndTomorrow['total_population'][1])

