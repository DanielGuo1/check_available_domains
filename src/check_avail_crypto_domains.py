""" This Script consumes the Domainr API.

The text File all_cryptos_from_cnc.txt (created via get_crypto_names.py and parsed via parse_crypto_names.py)
contains the top 5000 Cryptocurrencies at coinmarketcap.com. In this Script we will check if any of those domains is
still available to buy (e.g. ethereum.com).
"""
import csv
import requests

url = "https://domainr.p.rapidapi.com/v2/status"

headers = {
    'x-rapidapi-key': "YOUR_API_KEY",
    'x-rapidapi-host': "domainr.p.rapidapi.com"
}

domain_list = []

# search for every domain in this list (e.g. bitcoin.com, ethereum.com,...)
f = open("../data/all_cryptos_from_cnc.txt", "r")
domain_list.extend(f.read().splitlines())

for domain in domain_list:
    querystring = {"mashape-key": "YOUR_RAKUTEN_RAPID_API_KEY", "domain": domain.replace(" ", "") + ".com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()

    # save domain and status in external file for further analysis
    for elem in response['status']:
        with open('../data/available_coin_domains.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([elem['domain'], elem['status']])

