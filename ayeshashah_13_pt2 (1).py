#!/usr/bin/env python
# coding: utf-8

# ### PT2
# 

# ### VIVA QUESTIONS

# 1. What is the difference between both the codes and what will be the output from the following
#    codes if applied to a list of numbers
# 
# 
# 

# In[4]:


#a) For I in range (0,4): print I
list = [1,2,3,4]
for I in range(0,4):
    print(I)


# In[3]:


#b) For I in list: print I
for i in list:
    print(i)


# ans) Therefore, (a) will print numbers from 0 to 3 according to range as numbers while (b) will give output as elements present in the list of numbers defined above

# 2.	What is the output for the following
# word=’abcdefghij’
# word[:3]+word[3:]
# 

# In[6]:


word ='abcdefghij'
word[:3]+word[3:]


# 3.	How do you convert a list (containing words) to string 

# In[7]:


list1 = ['hello','world']
listToStr = ' '.join(map(str, list1))
listToStr


# ### PROGRAMMING QUESTIONS

# Q1.a) Input a list of 10 numbers from user. Identify prime, even, odd, positive, negative numbers and 0’s in the list. Store these  number in individual list and print all the list even if a list is empty.

# In[21]:


list1 = [] 
for i in range(0, 10): 
    ele = int(input()) 
  
    list1.append(ele) 
      
print(list1) 

prime=[]
even=[]
odd=[]
positive=[]
negative=[]
zero=[]

for i in list1:
    isprime = True
    for num in range(2,i):
        if i % num == 0:
            isprime = False
            
    if  isprime:
        prime.append(i)
    
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    if(i>0):
        positive.append(i)
    elif(i==0):
        zero.append(i)
    else:
        negative.append(i)
        
print("primes are :",prime)
print("even:",even)
print("odd:",odd)
print("positive:",positive)
print("negative:",negative)
print("zeroes:",zero)


# b) Merge all the list in the following order: zero’s, positive num, even num’s, negative num’s, odd num’s and prime num’s

# In[23]:


final_list=zero+positive+even+negative+odd+prime
final_list


# c) Sort the list in ascending order using bubble sort and print it by making a sort function.

# In[24]:


def bubbleSort(arr):
    n = len(arr)
         # Traverse through all array elements
    for i in range(n):
            # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element\n",
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(final_list)
print(final_list)
        


# In[ ]:




