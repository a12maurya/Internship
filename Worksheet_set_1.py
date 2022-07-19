#!/usr/bin/env python
# coding: utf-8

# # Worksheet_set_1

# Write a python program to find the factorial of a number.

# In[10]:


num = int(input("Enter a number: "))


factorial = 1


if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#  Write a python program to find whether a number is prime or composite.

# In[11]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


#  Write a python program to check whether a given string is palindrome or not.

# In[12]:


my_string=input("Enter string:")
if(my_string==my_string[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")


#  Write a Python program to get the third side of right-angled triangle from two given sides.

# In[13]:


def triangle (opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(triangle(3,4,'x'))
print(triangle(3,'x',5))
print(triangle('x',4,5))
print(triangle(3,4,5))


#  Write a python program to print the frequency of each of the characters present in a given string.

# In[14]:


strA = "timeofeffort"
print("Given String: ",strA)

res = {}

res={n: strA.count(n) for n in set(strA)}


print("Frequency of each character :\n ",res)


# In[ ]:




