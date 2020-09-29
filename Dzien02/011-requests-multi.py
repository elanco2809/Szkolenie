import requests as req
from multiprocessing.pool import ThreadPool
import time

response = req.get("http://51.91.120.89/TABLICE/")
lines = response.text.split("\n")
urls = ["http://51.91.120.89/TABLICE/"+line.strip() for line in lines][:10]
print(urls)

def download_url(url):
    r = req.get(url)
    file_name = url.split("/")[-1]
    with open("images/"+file_name, "wb") as fd:
        fd.write(r.content)
        print("save:",url)

ts1 = time.time()
result = ThreadPool(50).imap_unordered(download_url, urls)
for r in result:
    pass
ts2 = time.time()
print(f"{ts2-ts1}")
