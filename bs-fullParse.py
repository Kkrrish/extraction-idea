from bs4 import BeautifulSoup
import urllib
import webbrowser
import numpy as np
#r = urllib.urlopen('http://bothraclasses.com/evalution-report').read()
#soup = BeautifulSoup(r)
soup=BeautifulSoup(open("Bothra Classes | Student Evaluation Report.html"))
flag=0
#print(soup.prettify())
#print(type(soup))
#print(soup.find_all('tr'))
tr=soup.find_all('tr')
print len(tr)
for i in range(0,len(tr)):
	print i
	print tr[i]

print "Now trying to find given test code"
#test_code=raw_input()
#test_code=6203
test_index=input("Which test results do you want:" )	

foundCode=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[1].contents[0]
rank=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[4].contents[0]
score=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[3].contents[0]
print foundCode
print rank
print score
