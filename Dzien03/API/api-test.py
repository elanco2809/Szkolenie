import requests

resp = requests.post("http://127.0.0.1:5000/login", params={
    "user" : "admin",
    "pass" : "qwerty123"
})

print(resp.status_code)
print(resp.headers.get("Content-Type"))
print(resp.text)
