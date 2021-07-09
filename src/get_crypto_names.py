""" Gets Name and Ticker of Top 5000 Cryptocurrencies.

This Script saves all cryptocurrencie names from coinmarketcap to a file
using the coinmarketcap API.
"""
import json

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    # save to json
    with open('../data/coinmarketcap.txt', 'w') as outfile:
        json.dump(data, outfile)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
