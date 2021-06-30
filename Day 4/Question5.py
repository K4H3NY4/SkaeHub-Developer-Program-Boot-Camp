#Banner Image
from clint.textui import puts, colored, indent
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 5'))

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print(colored.blue("Delivering presents to"), house)
    deliver_presents_iteratively()

deliver_presents_iteratively()