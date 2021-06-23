# Write a Python program to send a request to a web page, and print the response text
# and content. Also get the raw socket response from the server.

#return 200 if successful (http codes)

import requests

url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'
key_value = {'mainurl': 'twitter.com'}

x = requests.post(url, data = key_value)
print('Server Response Code:',x.status_code)
print(x.text)