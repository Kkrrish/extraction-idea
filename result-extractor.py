from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib

#Variables

#Display and driver setting
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()

#Getting baseurl
driver.get('http://bothraclasses.com/evalution-report/')
assert "Student Evaluation Report" in driver.title
html_source=driver.page_source
page=html_source.encode('utf-8')
print "Original Page"
print page

#Giving required response
elem=driver.find_element_by_name('rollno')
elem.clear()
elem.send_keys("87095")
elem.send_keys(Keys.RETURN)
html_source=driver.page_source
page=html_source.encode('utf-8')
print "Result Page"
print page

#Just to check validity
"""try:
	assert "Invalid Roll Number" in html_source
except:
	flag=1
if flag=1:
	pass
else :
"""
#Now onto BeautifulSoup!
#"""

soup=BeautifulSoup(page)
print(soup.prettify())
#print(type(soup))

#Trial prints
tr=soup.find_all('tr')
print len(tr)
for i in range(0,len(tr)):
	print i
	print tr[i]

print "Now trying to find given test code"
#test_code=6203
test_index=input("Which test results do you want:" )	

#Navigating down to the required test tr
foundCode=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[1].contents[0]
rank=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[4].contents[0]
score=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[3].contents[0]
print foundCode
print rank
print score
#"""