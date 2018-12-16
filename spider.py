from bs4 import BeautifulSoup
import requests
import re

feasible = 'https://www.mywenxue.com'
start_url = 'https://www.mywenxue.com/xiaoshuo/132/132746/55793238.htm'

url = start_url
with open('novel.txt', 'w', encoding = 'utf8') as f:
	while re.match('.*Index\.htm$', url) == None:
		r = requests.get(url)

		s = BeautifulSoup(r.text, 'lxml')
		next = s.find(class_='r').a['href']
		url = feasible + next

		title = s.h2.text
		print(title)
		f.write(title + '\n')
		for article in s.find(class_='txt'):
			if article.string != None:
				f.write(article.string + '\n')
				
f.close()
			




