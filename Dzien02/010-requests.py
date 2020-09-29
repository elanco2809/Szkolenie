import requests as req
from requests.auth import HTTPBasicAuth

response = req.get("https://api.github.com/")
if response.status_code==200:
    print("ok")
else:
    print("coś innego")

print(response.content) #surówka bajtowa
print(response.text) #reprezentacja tesktowa odpowiedzi
data_json = response.json()

url = "https://api.github.com/search/repositories"
response = req.get(url,
                   params={"q" : "request+language:python"},
                   headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0"})

json_reponse = response.json()

#
response = req.post("https://httpbin.org/post", data={"key":"value"})
print(response.json())

# basic auth
url = "https://api.ambra.com.pl/j3GsmoZgcL/260/CQ02.png"
response = req.get(url, auth=HTTPBasicAuth('service','alamakota'),
                   allow_redirects=True, verify=False, timeout=(10, 15) )
file_name = url.split("/")[-1]
with open(file_name, "wb") as fd:
    fd.write(response.content)
print(response)

print("="*80)
# upload pliku
with open("CQ02.png","rb") as fd:
    file_dict = { "CQ02.png": fd }
    response = req.post("https://httpbin.org/post", files=file_dict)
    print(response.json())