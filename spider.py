from bs4 import BeautifulSoup
import requests

feasible = 'https://www.mywenxue.com'
start_url = 'https://www.mywenxue.com/xiaoshuo/132/132746/55793238.htm'

url = start_url

while url
r = requests.get(url)

s = BeautifulSoup(r.text, 'lxml')
next = s.find(class_='r').a['href']
url = feasible + next

for article in s.find(class_='txt'):
	if article.string != None:
		#print(article.string)
		print('dd')





