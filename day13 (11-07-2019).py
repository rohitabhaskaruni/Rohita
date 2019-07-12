#!/usr/bin/env python
# coding: utf-8

# ## Objectives  :
# ### 1. Functions
# ### 2. Iterators
# ### 3. Arrays
# 

# #### Functions : 
# ### Built- in and user-defined functions 
# ### Built- in functions --> print() , input() , range()
# ### user-defined functions -->
# ### Syntax :
# ####            def name_of_the_function(variable names) :
# ###                             ...........................
# ####                                 return statement (optional)

# In[5]:


# Addition of two numbrs function
def Addition(x,y) :
    sum= x+y
    return sum 
Addition(10,20) #function  calling 


# In[17]:


# Find area and perimeter of a circle using functions.
def area(r):
    return 3.14*r*r
def perimeter(r) :
    return 3.14*2*r
print(area(2))
print(perimeter(3))
    
      


# In[16]:


# Square and cube of a number
# x--> 5 square -->x*x cube-->x*square(x)
def square(x) :
    return x*x
def cube(x) :
    return x* square(x)
cube(5)


# In[3]:


def square(x) :
    print(x*x)
def cube(x) :
    print(x*x*x)
cube(5)
square(5)


# ### Anonymous functions --> Single line functions are called anonymous functions--> lambda

# In[5]:


Addition=lambda x,y : x+y
Addition(10,20)


# In[8]:


def Addition(x,y):
   return x+y
Addition(10,20)


# In[ ]:


help("modules")


# In[1]:


help("math")


# In[4]:


import math as m
print(m.sqrt(16))
print(m.factorial(5))


# In[6]:


from math import*
print(sqrt(16))
print(factorial(5))
print(fmod(5,2)) # returns remainder
print(gcd(4,6)) #greatest common deviser


# In[7]:


import time
print(time.asctime())
print(time.clock())
print(time.ctime())


# ### Iterators : string, list, tuple, set and dictionary

# In[18]:


#string
x=10 #integer
y=20.56 #float
z=5+8j #complex
b=true #boolean
f=false #boolean
name="rohita123" #string


# In[22]:


str1= "abcxyz"
str2="123"
print(str1[1]) #slice operator
print(str1[3:]) #slice range operator
print(str1+str2) #concatination
print(str1*3) #repetition
print('rohita' in str1) #membership operators
print ("rohta" not in str1)


# In[23]:


name="string"
course='python'
course[2]= 'z'
print(course) #python


# 

# ### Built-in functions :
# ### 1. len() --> returns length of string 
# ### 2. min ()
# ### 3. max()
# ### 4. str()

# In[24]:


str1= "abcxyz"
print(len(str1))
print(min(str1))
print(max(str1))
x=10 #integer
print(type(x)) #list
x=str(x)
print(type(x)) #str


# In[25]:


str1="abcABC123"
min(str1)


# In[26]:


help(str)


# In[28]:


str1="abc"
str1.capitalize()


# In[29]:


for i in range(1,11,2):
    print(i)


# In[ ]:




