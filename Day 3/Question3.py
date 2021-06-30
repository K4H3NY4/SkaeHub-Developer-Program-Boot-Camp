#import numpy
#

import numpy as np
print("Enter numbers separated by a (,) e.g. 1,2,3,4 : ")
list_input = input()
n = np.array(list_input)


print(n)
print('Size of memory occupied: ')
print('%d bytes' %(n.size * n.itemsize))
