from urllib.request import urlopen 
from urllib.request import Request
from bs4 import BeautifulSoup as soup


#File-to write to
filename = 'movie_list.csv'
f = open(filename,'w')
headers = "Movie-name, Quality , Link\n"

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
	raw_url = 'https://www1.yesmovies.gg/movie/filter/movie/all/all/all/all/latest/' + "?page=" + str(i)
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
	#containers = page_soup.findAll("div",{'class':"ml-item"})
	anchors = page_soup.findAll("a",{"class":"ml-mask jt"})

		
	
	# info = anchors[0].text.split('\n')
	# print(shipping)

	for anchor in anchors:
		#print(anchors[0]['href'])
		temp = anchor.text.split('\n')
		temp = [x for x in temp if x != '']
		quality = temp[0]
		title = temp[1]
		href = "www2.yesmovies.gg" + anchor['href']
		
		quality = quality.replace(' ','-')
		quality = quality.replace(',','-')
		title = title.replace(' ','-')
		title = title.replace(',','-')

		#print("%s,%s,%s"%(href,title,quality))
		f.write(title + "," + quality + "," + href + "\n")

print('mission accomplished ...')
f.close()	
