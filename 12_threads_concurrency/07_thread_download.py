import threading
import requests
import time

def download(url):
    print(f"Starting Downloading from {url}")
    resp = requests.get(url)
    print(f"Ending Downloading from {url}, size {len(resp.content)} bytes")
    with open(f"{url.split('/')[-1]}.jpg", "wb") as file:
        file.write(resp.content)

urls = [
     "https://httpbin.org/image/jpeg",
     "https://httpbin.org/image/png",
     "https://httpbin.org/image/svg",
]

start= time.time()
threads=[]

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(threads)

print(f"All downloads done in {end-start:.2f} seconds")