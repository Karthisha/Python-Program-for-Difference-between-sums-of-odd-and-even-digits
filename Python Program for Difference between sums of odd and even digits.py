#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to check if difference between sum of
# odd digits and sum of even digits is 0 or not
 
# Reading Input
num = int(input())
string1 = str(num)
evensum = 0
oddsum = 0
 
 
# Driver Code
for i in range(0, len(string1)):
    if(i % 2 == 0):
        evensum += int(string1[i])
    else:
        oddsum += int(string1[i])
 
 
# Condition
if(oddsum-evensum == 0):
    print("Yes")
else:
    print("No")


# In[ ]:




