import csv
import re
import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen

from torrents import *
#from convert import *


search = input()
links=getLinks(search)

#fd1 = open('./Boys.csv', 'w')
#writer = csv.writer(fd1, delimiter=',')

for url in links:
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	source = urlopen(req).read()
	soup = bs.BeautifulSoup(source, 'lxml')
	detailsframe = soup.find('div', id=re.compile('detailsframe'))
	Mdiv = detailsframe.find('div', {'class':'download'})
	dl2 = detailsframe.find('dl', {'class':'col2'})
	dd = dl2.find_all('dd')
	Mlink = Mdiv.find('a').get('href')

	title = detailsframe.find('div', id=re.compile('title')).string.strip()
	#Dlink = getDownloadLink(Mlink)
	uploaded = dd[0].string.strip()
	seeders = dd[2].string.strip()
	leechers = dd[3].string.strip()
	print (title)
	print ('\n')
	print (Mlink)
	print ('\n\n\n')