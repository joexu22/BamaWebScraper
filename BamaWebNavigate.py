# selenium files
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# headless files
from pyvirtualdisplay import Display

# sqlite3 files
import sqlite3
import sys

# TODO: make this file an importable class file

# headless display
# display = Display(visible=0, size=(800,600))
# display.start()

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
