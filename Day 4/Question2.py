# The Haversine formula calculates the great-circle distance between two points. 
# Start by calculating the change in latitude and longitude, in radians, 
# and input the result into the Haversine formula (implemented below). 
# Use the functions in the math library for trigonometry related calculations. 

import math
from geopy.geocoders import Nominatim

#Banner Image
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 2'))

#initialize the Nominatim
geolocator = Nominatim(user_agent="Question 2")

#this code retrives map data from the string
location1 = geolocator.geocode("Nairobi")
location2 = geolocator.geocode("Cairo")

#this print function displays the specific lat and long
print((location1.latitude, location1.longitude))

#Haversine formula starts
lat1 = location1.latitude

lon1 = location1.longitude

lat2 = location2.latitude

lon2 = location2.longitude

dlon = lon2 - lon1

dlat = lat2 - lat1


a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#Define earth's radis
R = 6373.0

distance = R * c


print(int(distance), 'KM')