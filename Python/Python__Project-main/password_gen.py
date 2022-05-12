'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''


# It is  an alternative method for generating password
# In this method string module is not required

import random

upper_letr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letr = "abcdefghijklmnopqrstuvwxyz"
num = 0,1,2,3,4,5,6,7,8,9
punc = "~!@#$%^&*()_+|/?.,<>{ }:'"
inp = int(input("Enter the length of the password : "))

s = []

s.extend(str(upper_letr))
s.extend(str(lower_letr))
s.extend(str(num))
s.extend(str(punc))

random.shuffle(s)


print("".join(s[0:inp]))


