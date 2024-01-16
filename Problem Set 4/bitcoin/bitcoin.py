import requests
from sys import argv,exit

try:
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    exit()

a = res.json()
price = float(a["bpi"]["USD"]["rate"].replace(',' ,''))
if len(argv) != 2:
    exit('Missing command-line argument')
else:
    try:
        i = float(argv[1])
    except:
        exit('Command-line argument is not a number')



amount = i*price
print(f"${amount:,.4f}")
