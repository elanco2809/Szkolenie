import grequests as req
import time

response = req.get("http://51.91.120.89/TABLICE/")


lines = req.map([response])[0].text.split("\n")
urls = ["http://51.91.120.89/TABLICE/"+line.strip() for line in lines if len(line.strip())>0 ][-10:]
print(urls)

ts1 = time.time()
reqs = [req.get(url) for url in urls]
result = req.map(reqs)
ts2 = time.time()
print(f"{ts2-ts1}")
for r in result:
    file_name = r.url.split("/")[-1]
    with open("images/"+file_name, "wb") as fd:
        fd.write(r.content)
        print("save:",r.url)

