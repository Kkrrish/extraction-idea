from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
import csv

#Variables
flag=0
outRow=[[0,0,0,0]]

#with open('results.csv', 'wb') as csvfile:
#	results=csv.writer(csvfile,delimeter=' ', quotechar='|', quoting=csv.QUOTE_MINUMAL)
results=csv.writer(open("results.csv","w"))
results.writerow(["Roll Number", "Test Code", "Rank", "Marks"])

#Display and driver setting
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()

test_index=input("Which test results do you want:" )	
print "Sure, just a minute.."
#Getting baseurl
driver.get('http://bothraclasses.com/evalution-report/')
assert "Student Evaluation Report" in driver.title
html_source=driver.page_source
page=html_source.encode('utf-8')
print "Navigated to Bothra Classes Result Page"
#print page

print "Getting the results.."

for x in range(0,10):
	for y in range(0,10):
		rollno=87000+10*x+y
		#Giving required response
		elem=driver.find_element_by_name('rollno')
		elem.clear()
		elem.send_keys(str(rollno))
		elem.send_keys(Keys.RETURN)
		html_source=driver.page_source
		page=html_source.encode('utf-8')
		#print "Result Page"
		#print page

		#Now onto BeautifulSoup!
		
		soup=BeautifulSoup(page)
		#print(soup.prettify())
		#print(type(soup))

		tr=soup.find_all('tr')

		#For Validity
		if len(tr)<13:
			flag=1
		else:
			#print "Now trying to find given test code"
			#test_code=6203
			
			#Navigating down to the required test tr
			foundCode=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[1].contents[0]
			rank=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[4].contents[0]
			score=soup.find_all('tr')[len(tr)-2-test_index].find_all('td')[3].contents[0]
			print str(rollno)+" "+str(foundCode)+" "+str(rank)+" "+str(score)
			#results=csv.writer(open("results.csv","w"))
			results.writerow([int(rollno),int(foundCode),int(rank),int(score)])
			#print foundCode
			#print rank
			#print score
			#"""
