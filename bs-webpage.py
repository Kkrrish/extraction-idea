from bs4 import BeautifulSoup
import urllib
import webbrowser

r = urllib.urlopen('http://bothraclasses.com/evalution-report').read()
soup = BeautifulSoup(r)

#print(soup.prettify())
#print(type(soup))
print(soup.find_all('script'))
