# Write a Python code to send a request to a web page and stop waiting for a response
# after a given number of seconds. In the event of a time out on the request, raise the
# timeout exception.

import requests

print('Enter number of seconds')
seconds = float(input())

try:
    url = 'https://infama-api.pacisvorgel.co.ke/public/api/links'

    x =requests.get(url, timeout = seconds)
    print('Server Response Code:',x.status_code)
    print(x.text)

except requests.exceptions.RequestException as e:
    print(e)    