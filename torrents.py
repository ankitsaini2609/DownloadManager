import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen

def getLinks(search):
	search = search.strip()
	search = search.replace(" ", "+")

	url = 'https://piratebay.red/s/?q='+search+'&category=0&page=0&orderby=99/'

	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	source = urlopen(req).read()

	soup = bs.BeautifulSoup(source, 'lxml')
	table = soup.find_all('a')

	list_link=[]
	for row in table:
	    list_link.append(row.get('href'))

	lists = filter(lambda x:x.startswith('/torrent/'), list_link)
	fd = open('links.txt', 'w')
	links=[]
	for row in lists:
		s = 'https://piratebay.red'+row
		fd.write(s+'\n')
		links.append(s)
	return links