import urllib3
import json

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
try:
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    data = json.loads(r.data.decode())
    print(data)
    rates = data[0]["rates"]
    for rate in rates:
        print(f"{rate['currency']}, {rate['code']} = {rate['mid']}")
except Exception as exc:
    print(exc)
