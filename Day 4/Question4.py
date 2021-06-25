from geopy.geocoders import Nominatim
#Banner Image
from pyfiglet import Figlet
f = Figlet(font='big')
print (f.renderText('Question 4'))


#
geolocator = Nominatim(user_agent="question1")

#Prompt user to enter zip for Kenya one must add Town name then the zip code
print('Enter a State/ Town name')
entered_state = input()
print("\nCountry:",entered_state)

#Pass state to geolocator(nominatim) function
#geocode resolves a location from a string
location = geolocator.geocode(entered_state)
##print("Details of the said pincode:")
details = location.address

country = details.split(',')
print(country[-1])
