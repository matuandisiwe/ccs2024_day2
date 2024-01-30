#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:14:02 2024

@author: andisiwematu


"""

#three main types of data

"""  
1. int - interger - whole number
2.float - number with decimals
string - letters, text, words
paragraphs

"""


import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
df = pandas.DataFrame(file)

"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 - whole number
 1   Gender   11 non-null     object - string
 2   Country  11 non-null     object - string
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes
None """

print(df.describe())
 

""""             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""
#Practice

file1 = pandas.read_csv("iris.csv")
print(file1)
print(file1.info())
df = pandas.DataFrame(file1)

"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64 - float
 1   sepal_width   150 non-null    float64 - float
 2   petal_length  150 non-null    float64 - float
 3   petal_width   150 non-null    float64 - float
 4   species       150 non-null    object  - string
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None
"""

print(df.describe())


"""       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

"""

file2 = pandas.read_csv("diab_data.csv")
print(file2)
print(file2.info())
df = pandas.DataFrame(file2)
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
None"""

print(df.describe())
""""preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
"""

file3 = pandas.read_csv("insurance_data.csv")
file3 = pandas.read_csv("insurance_data.csv", skiprows=5)
print(file3)
print(file3.info())

"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 63 entries, 0 to 62
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   X       63 non-null     int64  
 1   Y       63 non-null     float64
dtypes: float64(1), int64(1)
memory usage: 1.1 KB
None"""
df = pandas.DataFrame(file3)



print(df.describe())

file4 = pandas.read_csv("housing_data.csv")
print(file4)
print(file4.info())
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 505 entries, 0 to 504
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.4 KB
None"""
df = pandas.DataFrame(file4)

print(df.describe())

"""  0.00632          18        2.31  ...       396.9        4.98          24
count  505.000000  505.000000  505.000000  ...  505.000000  505.000000  451.000000
mean     1.271696   13.285941    9.218812  ...  332.664158   11.550792   23.749889
std      2.400926   23.070598    7.170151  ...  125.414151    6.063900    8.818376
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049810    0.000000    3.440000  ...  364.610000    6.900000   18.500000
50%      0.144760    0.000000    6.960000  ...  390.640000   10.400000   21.900000
75%      0.825260   18.100000   18.100000  ...  395.600000   15.020000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

[8 rows x 14 columns]"""

column_names =["A","B","C","D","E","F","G","H","I"]
file5= pandas.read_csv("housing_data.csv",names=column_names)
print(file5)
#Storing Data in Python

"""Storing data in python 
1. List
2. Dictionaries
3. Data Frame

"""
file = pandas.read_csv("country_data.csv")

print(file)
 

age1 = 30
age2 = 25
age3 = 29


B1 =30
B2 =40
B3 =30
B4 =49


print(B1)
print(B2)


#Using list
age=[30,40,30,49,22,35,22,46,29,25,39]
print(age)

# List indexes start at 0 which has the value 30

print(age[0])
print(age[1])
print(age[10])


#Basic stats
age=[30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)


#Storing text

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

gender = ["M","M","F","M","F","F","F","M","M","F","M"]

print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

#Country list

country = ["South Africa","Botswana","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])


#Data storage with list

my_list =[42, -2021,6.283,"tau","node"]
print(my_list)

#To add a new variale

print(my_list[:])
my_list.append("pi")
print(my_list)

#To insert a new variable at a specific position

my_list.insert(1,"pi2")
print(my_list)

#To remove variable from the list

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])

#Dictionaries

"""""Dictionaries - key: value pairs"""

d ={'key1':'value1','key2':'value2'}
person = {'name':'Jon Doe', 'age':30, 'address':'123 Main St.'}
print(person['name'])
print(person.get('age'))

person['phone']= '555-555-5555'

print(person)

#Data frame


data={'age':[30,40,30,49,22,35,22,46,29,25,39],'gender': ["M","M","F","M","F","F","F","M","M","F","M"],'country':["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]}

df = pandas.DataFrame(data)

print(df)

import pandas as pd

df =pd.DataFrame(data)

print(df['gender'])
print(df[df['age']>30])

height = [11,15,16,18,18,19,29,20,18,13,11]

df['height']=height
 
print(df)


#removing a column from dataframe

df.drop(column=[''], inplace=TRUYE)


