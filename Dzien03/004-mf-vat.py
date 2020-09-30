import urllib3
import json
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
nip = "5272538935"
url = f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={today}"
try:
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    data = json.loads(r.data.decode())
    if data.get("code"):
        print(f"Error {data.get('code')} = {data.get('message')}")
    else:
        subject = data["result"]["subject"]
        print(subject["name"])
        print(subject["statusVat"])
        print(subject["accountNumbers"])
except Exception as exc:
    print(exc)
