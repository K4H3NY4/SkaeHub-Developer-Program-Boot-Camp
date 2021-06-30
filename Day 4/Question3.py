# Write a Python function to get the city, state and
# country name of a specified latitude and longitude using Nominatim 
# API and Geopy package.

import math
from geopy.geocoders import Nominatim

#Banner Image
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 3'))

geolocator = Nominatim(user_agent='question3')


location1 = geolocator.reverse("-1.3031689499999999, 36.826061224105075")
print(location1.address)