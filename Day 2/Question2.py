#Write a Python program to check if a number is a perfect square.

from math import sqrt
print('Enter Number:')
square = int(input())

#find square root of input
square_root = sqrt(square)
print(square_root)

if( square == square_root*square_root):
   print (isinstance(square_root, int))
else:
    print (isinstance(square_root, int))
