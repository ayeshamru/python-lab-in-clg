#!/usr/bin/env python
# coding: utf-8

# # ***MINI PROJECT***
# __________
# ## <span style='color:Green'>PASSWORD GENERATOR</span>
# __________
# ## <span style='background :yellow' >THIS SYSTEM CREATES 3 PASSWORDS AT ONCE  </span>

# **
# # GROUP MEMBERS :-
# ### NAME : AYESHA SHAH
# ### ROLLNO : 2K18CSUN01013
# ### NAME : HIRDYANSH DUDI
# ### ROLLNO : 2K18CSUN01020
# **

# In[1]:


import random

#A function to shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program 
def password_string():
    uppercaseLetter1=chr(random.randint(65,90)) 
    uppercaseLetter2=chr(random.randint(65,90)) 
    lowercaseLetter1=chr(random.randint(97,122))
    lowercaseLetter2=chr(random.randint(97,122))
    digit1=chr(random.randint(48,57))
    digit2=chr(random.randint(48,57))
    specialchar1=chr(random.randint(33,38))
    specialchar2=chr(random.randint(33,38))

    #Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + specialchar1 + specialchar2
    password = shuffle(password)
    print("Password : ",password)

for i in range(1,4):
    password_string()


# In[ ]:




