# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:10:05 2023

@author: Nikitha
"""

x=90
y=78
sum=x+y
print("sum  of {} and {} is {}".format(x,y,sum))
print("sum of %d and %d is %d"%(x,y,sum))#percentile specifier
print("----------------------")
s=" hi i am nikitha"
s1=s.split()
print(s1)#splliting a string
s2=s.split("t")#seperating t see output
print(s2)
print("--------------------")
s="-"
print(s.join("nikitha"))#join - in between nikitha each char between
print("--------------")
# write a program to add individual digits(100-999)
num=897
r=num%10#r=7
a=num//10#a=89
b=a%10#b=9
c=a//10#c=8
sum=r+b+c;
print("sum=",sum)
print("----------------------------------")
num=987
r=num%10
a=num//10
b=a%10#my code worked
c=a//10
sum=r+b+c
print("sum is=",sum)
print("---------------------------------")
num=999#my code worked
r=num//100
a=r%10
b=num%10
sum=r+a+b
print("sum is:",sum)

