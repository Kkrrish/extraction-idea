from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('http://bothraclasses.com/evalution-report').read()
soup = BeautifulSoup(r)

print(soup.prettify())