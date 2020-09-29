import requests as req

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
