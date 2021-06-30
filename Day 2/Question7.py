# Create a Python project to read public data returned from URL, and parsing JSON to a
# dictionary object.

import requests
import json

url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'

x =requests.get(url)
print(x.json())

with open("links.json", "w") as outfile:
    json.dump(x.json(), outfile)

