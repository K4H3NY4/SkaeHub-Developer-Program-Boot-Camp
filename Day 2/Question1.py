#Write a Python program to check if a given positive integer is a power of four.
#modulas % 4

print('Enter Number')
number = int(input())

if (number%4 == 0):
    print(number, 'is a power of 4')
else:
     print(number , 'is not a power of 4')