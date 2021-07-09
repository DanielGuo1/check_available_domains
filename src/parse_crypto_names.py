""" Parse the received data from coinmarketcap (coinmarketcap.txt).

For this analysis only the name and the ticker of the cryptocurrencie is important.
Therefore we clean the output.
"""
import json

with open('../data/coinmarketcap.txt') as json_file:
    data = json.load(json_file)
    for p in data['data']:
        print('Name: ' + p['name'])
        print('Website: ' + p['symbol'])
        with open('../data/all_cryptos_from_cnc.txt', 'a') as f:
            f.write(p['name'])
            f.write('\n')
            f.write(p['symbol'])
            f.write('\n')
