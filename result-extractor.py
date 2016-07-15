from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
import csv

#Variables
flag=0

results=csv.writer(open("results.csv","w"))

#Display and driver setting
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()

test_code=input("Which test results do you want(give test code): " )	
results.writerow(["Test",int(test_code)])
results.writerow(["Roll Number", "Rank", "Marks"])
print "Sure, Navigating to Bothra Classes webpage.."
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
		if len(tr)<=6:
			flag=1
		elif rollno==87096:
			flag=1
		else:
			#test_code=6203
			
			#Navigating down to the required test tr
			for i in range(1,len(tr)-10):
				foundCode=soup.find_all('tr')[len(tr)-2-i].find_all('td')[1].contents[0]
				if str(foundCode)==str(test_code) :
					rank=soup.find_all('tr')[len(tr)-2-i].find_all('td')[4].contents[0]
					score=soup.find_all('tr')[len(tr)-2-i].find_all('td')[3].contents[0]
					print str(rollno)+" "+str(rank)+" "+str(score)
					#results=csv.writer(open("results.csv","w"))
					results.writerow([int(rollno),int(rank),int(score)])
					#print foundCode
					#print rank
					#print score
					#"""
				else:
					pass

#Ho gaya, ab style marte hai
print "Done"
print "Results are stored in 'results.csv'."