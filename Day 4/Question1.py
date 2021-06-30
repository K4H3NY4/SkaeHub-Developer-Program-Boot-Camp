from geopy.geocoders import Nominatim

#Banner Image
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 1'))

#initialize  nominatim
geolocator = Nominatim(user_agent="question1")

#Prompt user to enter zip for Kenya one must add Town name then the zip code
print('Enter zip code e.g Nairobi 00502')
zipcode = input()
print("\nZipcode:",zipcode)

#Pass zipcode to geolocator(nominatim) function
#geocode resolves a location from a string
location = geolocator.geocode(zipcode)
print("Details of the said pincode:")
print(location.address)

details = location.address

country = details.split(',')
print(country[-1])
