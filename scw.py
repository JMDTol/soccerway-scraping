import requests
from bs4 import BeautifulSoup

page = requests.get("http://au.soccerway.com/national/australia/a-league/2005-2006/regular-season/r2080/")

if page.status_code == 200:
	print("sucessfully grabbed page..")
else:
	print("something went wrong with this page...")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

print(list(soup.children))


