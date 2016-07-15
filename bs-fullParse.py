from bs4 import BeautifulSoup
import urllib
import webbrowser

#r = urllib.urlopen('http://bothraclasses.com/evalution-report').read()
#soup = BeautifulSoup(r)
soup=BeautifulSoup(open("Bothra Classes | Student Evaluation Report.html"))
test_code=raw_input()
#print(soup.prettify())
#print(type(soup))
#print(soup.find_all('tr'))
tr=soup.find_all('tr')
print len(tr)
for i in range(0,len(tr)):
	print i
	print tr[i]
