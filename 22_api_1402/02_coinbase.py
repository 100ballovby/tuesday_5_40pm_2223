import json
import requests as r


url = "https://api.coinbase.com/v2/exchange-rates"
ans = r.get(url)


def make_file(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))


def read_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


make_file("rates.json", ans.json())
rates = read_file("rates.json")

from_cur = input("Insert Currency code: ").upper()
amount = float(input("Amount of money: "))
exc_rate = float(rates['data']['rates'][from_cur])
print(f"{amount} {from_cur} in USD is = {amount / exc_rate}")
