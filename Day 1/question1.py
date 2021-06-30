#  nested if and modulas

def year(x):
    if (x%100 == 1 ):
     print(' Not Leap Year')
     leap = 0
     print(leap)
    elif( x%4 == 0 or x%400 == 0):
        leap = 1
        print(leap)
    else:
        leap = 0
        print(leap)

print('Enter Year')
a = int(input())

year(a)

