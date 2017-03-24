import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen

from torrents import *


search = input()
links=getLinks(search)

for l in links:
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	source = urlopen(req).read()

	soup = bs.BeautifulSoup(source, 'lxml')
	