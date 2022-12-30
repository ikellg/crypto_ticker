
import argparse
from datetime import datetime
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--symbol',
                    help='symbol you want price for')

args = parser.parse_args()

endpoint = "/api/v3/ticker/price"

url = "https://api.binance.us"

ticker_endpoint = f"{url}{endpoint}"

cur_results = float('inf')

print(f"Symbol: {args.symbol}")

while True:
    new_results = float(requests.get(ticker_endpoint, params={'symbol':args.symbol}).json()['price'])

    if new_results != cur_results:
        print(f"Price: {new_results} | Time: {datetime.now()}")
        cur_results = new_results
