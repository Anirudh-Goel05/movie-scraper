from urllib.request import urlopen 
from urllib.request import Request
from bs4 import BeautifulSoup as soup


#File-to write to
filename = 'indian_movie_list.csv'
f = open(filename,'w')
headers = "Movie-name, Quality\n"

f.write(headers)

while True:	
	y = int(input('Enter the number of pages till you want to search:'))
	if y <= 0:
		print('Page number must be >= 1')
	else:
		y += 1
		break	


print('fetching data from the website ...')
for i in range(1,y):
	# import urllib.request
	raw_url = 'https://www1.yesmovies.gg/country/india/' + "?page=" + str(i)
	my_url = Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})

	# Opening a new connection and grabing the page's html
	try:
		uClient = urlopen(my_url)
	except:
		break

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
		f.write(title + "," + quality + "\n")

print('mission accomplished ...')
f.close()	
