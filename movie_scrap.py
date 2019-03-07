from urllib.request import urlopen 
from urllib.request import Request
from bs4 import BeautifulSoup as soup


#File-to write to
filename = 'movie_list.csv'
f = open(filename,'w')
headers = "Movie-name, Quality\n"

f.write(headers)

# import urllib.request
my_url = Request('https://www1.yesmovies.gg/movie/filter/movie/all/all/all/all/latest/', headers={'User-Agent': 'Mozilla/5.0'})

# Opening a new connection and grabing the page's html
uClient = urlopen(my_url)

page_html = uClient.read()
uClient.close()

# Parsing the html page
page_soup = soup(page_html,'html.parser')

#Finding all containers from html dom examination
containers = page_soup.findAll("div",{'class':"ml-item"})

for container in containers:
	info = container.text.split('\n')
	info = [x for x in info if x != '']
	quality = info[0].replace(' ','-')
	quality = quality.replace(',','-')
	title = info[1].replace(' ','-')
	title = title.replace(',','-')
	# print(quality + " " + title)
	f.write(title + "," + quality + "\n")

f.close()
