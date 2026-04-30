import threading
import time
import requests

def task():
 print("Task başladı")
 time.sleep(3)
 print("Task bitdi")
thread = threading.Thread(target=task)
thread.start()
print("Main proqram davam edir")
thread.join()


def download_file(name):
 print(f"{name} başladı")
 time.sleep(2)
 print(f"{name} bitdi")
threads = []
for i in range(1, 6):
 t = threading.Thread(
 target=download_file,
 args=(f"file_{i}.txt",)
 )
 threads.append(t)
 t.start()
for t in threads:
 t.join()


websites = [
 "https://google.com",
 "https://github.com",
 "https://example.com"
]
def check(url):
    try:
        r = requests.get(url, timeout=5)
        print(url, r.status_code)
    except requests.RequestException:
        print(url, "işləmir")
threads = []
for url in websites:
    t = threading.Thread(target=check, args=(url,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()