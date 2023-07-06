# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:14:03 2023

@author: Nikitha
"""

l=[12,"nikitha"]#this is called list indexing is possible
print(l)
print(l[0:2])
print(l[::-1])#reversing the index values
l[1]=3 #it is mutable we are chaning nikitha to 3
print(l) # after changes it prints
d={7:'y',5:'u'}  # dictionary 7 is key u is value ,data is retrived with use of key not indexing
print(d[5])#prints the key value associated to 5
s={12,3,"hi"}# its a set not a sequential data type so indexing is not possible
print(s)
a=2
b=9
print("sum is:", a+b)
a1=int(input("enter a1"))
print(a1**0.5)#exponentation
t=(12,"nikitha")
print(t)# its immutable cant be changed
t[1]=3# its not changebale once its defined shows error