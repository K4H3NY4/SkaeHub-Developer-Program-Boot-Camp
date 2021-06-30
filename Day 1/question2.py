#Enter Statement
#Split the explode (split) the statement
#select last item in array
#get string length of last item


print('Enter a statement')

statement = input()

x = statement.split()

last_word = x[-1]
print(len(last_word))