# selenium files
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# headless files
from pyvirtualdisplay import Display

# sqlite3 files
import sqlite3
import sys

# beautiful soup
from bs4 import BeautifulSoup
import re

# TODO: make this file an importable class file

# headless display
# display = Display(visible=0, size=(800,600))
display = Display(visible=0)
display.start()

driver_location = "./chromedriver",
website_location = "https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype"

# Test Input
randomSchool = (u'Massachusetts', u'Univ of Massachusetts Lowell')
print randomSchool[0]
print randomSchool[1]

state = randomSchool[0]
school = randomSchool[1]

# TODO: switch statement allowing for any webdriver
driver = webdriver.Chrome("./chromedriver")
driver.get(website_location)

radio_button_css = "input[type='radio'][value='BAMANAME']"
bamaRadioBtn = driver.find_element_by_css_selector(radio_button_css)
bamaRadioBtn.click()
search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()

stateList = Select(driver.find_element_by_id("p_state"))
stateList.select_by_visible_text(state)

search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()

schoolList = Select(driver.find_element_by_id("p_sbgi"))
schoolList.select_by_visible_text(school)

search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()

textBox = driver.find_element_by_id('crse_name_input_id')
# TODO: make this into fillable form
# this code here makes it so that people can search for the school they want
# or just scrape the whole table for now...
textBox.send_keys("%")
# confirm that entering into the textbox works
# driver.get_screenshot_as_file('screenshot_1.png')
getCourseList_css = "input[type='submit'][value='Get Course List']"
courselistBtn = driver.find_element_by_css_selector(getCourseList_css)
courselistBtn.click()
# make sure that I'm at a scrapable page
# driver.get_screenshot_as_file('screenshot_2.png')

# getting the current html for beautiful soup
html_page = driver.page_source
soup = BeautifulSoup(html_page, 'lxml')

print soup
print "************"
test_regexp = re.compile("\w*Formal\w*")
testing = soup.find_all(text=test_regexp)
print testing

print "************"

# TODO: some smart string parsing algorithm here
class_regexp_1 = re.compile("\w*Formal\w*")
class_regexp_2 = re.compile("\w*Algor\w*")

target_class_1 = soup.find_all(text=class_regexp_1)
target_class_2 = soup.find_all(test=class_regexp_2)
target_class = target_class_1 + target_class_2
print(target_class)

# getting the name of the other type
for target_equivalency in target_class:
    try:
        print target_equivalency.parent.parent
    except AttributeError:
        # some error that I'm not expecting
        pass

# clean-up
driver.close()
