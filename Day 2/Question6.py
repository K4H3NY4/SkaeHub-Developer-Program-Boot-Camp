# Create a Python project to perform some simple statistics on a list of values
from statistics import mean

print('Enter Values separated by a comma')
data_value = input()

processed_list = data_value.split(',')

print(processed_list)


print('MAX',max(processed_list))
print('MIN',min(processed_list))
print('List Length',len(processed_list))
print('MIN',mean(processed_list))

