from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('http://bothraclasses.com/evalution-report/')
html_source=driver.page_source
page=html_source.encode('utf-8')
print page
elem=driver.find_element_by_name('rollno')
elem.clear()
elem.send_keys("87095")
elem.send_keys(Keys.RETURN)
html_source=driver.page_source
page=html_source.encode('utf-8')
print page
