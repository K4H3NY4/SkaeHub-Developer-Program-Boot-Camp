#Banner Image
from clint.textui import puts, colored, indent
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 7'))

game_score = [('Pong', 238), ('Snake', 98), ('Bounce', 397), ('Super Mario', 182)]
print("Original:")
print(game_score)

#shuffles the list of tuples using lambda
game_score.sort(key = lambda x: x[1])
print("\nSorted:")
print(game_score)