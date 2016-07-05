from bs4 import BeautifulSoup

soup=BeautifulSoup(open("trialPage.html"))

print(soup.prettify())