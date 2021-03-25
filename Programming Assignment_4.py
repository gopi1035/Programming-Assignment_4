#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Q1.Write a Python Program to Find the Factorial of a Number?
fact = 1
num = int(input("Enter a number: "))
for i in range(1,num + 1):
       fact = fact*i
print("The factorial of",num,"is",fact)


# In[12]:


#Q2.Write a Python Program to Display the multiplication Table?
num1= int(input("Enter a number: "))
sum=0
if num1<=10:
    for i in range(1,11):
        print(num1,"X",i,"=",i*num1)
else:
    for i in range(1,num1+1):
        print(num1,"X",i,"=",i*num1)


# In[13]:


#Q3.Write a Python Program to Print the Fibonacci sequence?
fib=int(input("Enter a number: "))
a=0
b=1
print(a)
print(b)
for i in range(3,fib+1):
    c=a+b
    a=b
    b=c
    print(c)


# In[26]:


#Q4.Write a Python Program to Check Armstrong Number?
#armstronog number#
arm= int(input("Entre a number: "))
sum= 0
temp=arm
while temp>0:
    digit =temp%10
    sum+=digit**3
    temp//=10
if arm==sum:
    print(arm, "is an armstrong number.")
else:
    print(arm," is not an armstrong number")


# In[49]:


#Q5.Write a Python Program to Find Armstrong Number in an Interval?
arm1=int(input("Enter Lower Number: "))
arm2=int(input("Enter Upper Number: "))
for k in range(arm1, arm2+1):
    order=len(str(k))
    sum=0
    temp = k
    while temp > 0:
        digit =temp%10
        sum+=digit**3
        temp//=10
    if k==sum:
        print(sum)
    else:
        pass


# In[44]:


#Q6.Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("Enter a natural number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


# In[ ]:




