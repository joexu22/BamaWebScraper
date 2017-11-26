from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO: solve the problem using levels of webscraping
# just code something

class bamaWebCrawler(object):
    """ A framework for navigating Bama's course equivalency website

    Attributes:
        TODO: Maybe having it inherit from a object with a selection of drivers
        driver: A hands off browser
        etc.
    """

    def __init__(self, driver_location = "./chromedriver",
                 website_location = "https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype"):
        self.driver_location = driver_location
        self.website_location = website_location
        self.driver = webdriver.Chrome("./chromedriver")

    def getToPickState(self):
        self.driver.get(self.website_location)
        radio_button_css = "input[type='radio'][value='BAMANAME']"
        bamaRadioBtn = self.driver.find_element_by_css_selector(radio_button_css)
        bamaRadioBtn.click()
        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(search_button_css)
        bamaSearchBtn.click()
        bamaState = Select(self.driver.find_element_by_id("p_state"))

# __main__ program here
dataCollector = bamaWebCrawler()
dataCollector.getToPickState()

# TODO: Database Solution...
state_list = []

def getToPickState():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype")
    radio_button_css = "input[type='radio'][value='BAMANAME']"
    bamaRadioBtn = driver.find_element_by_css_selector(radio_button_css)
    bamaRadioBtn.click()
    search_button_css = "input[type='submit'][value='Submit']"
    bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
    bamaSearchBtn.click()
    bamaState = Select(driver.find_element_by_id("p_state"))
    """
    for state in bamaState.options:
        bamaState.select_by_visible_text(state.text)
        WebDriverWait(driver, 60)
    """
    driver.quit()

# creating a function that takes me to the multiple options
def pickState():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype")
    radio_button_css = "input[type='radio'][value='BAMANAME']"
    bamaRadioBtn = driver.find_element_by_css_selector(radio_button_css)
    bamaRadioBtn.click()
    search_button_css = "input[type='submit'][value='Submit']"
    bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
    bamaSearchBtn.click()
    bamaState = Select(driver.find_element_by_id("p_state"))
    for state in bamaState.options:
        bamaState.select_by_visible_text(state.text)
        WebDriverWait(driver, 60)
    driver.quit()

#pickState()

"""
# creating a instance of Chrome driver
driver = webdriver.Chrome("./chromedriver")

# starting up an instance of the website
# TODO: have this in config file
# TODO: wondering if its better to have this starting point be google
driver.get("https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype")

# this suppose is used to manually check right now
print(driver.title)

# selecting radio-button
radio_button_css = "input[type='radio'][value='BAMANAME']"
bamaRadioBtn = driver.find_element_by_css_selector(radio_button_css)
bamaRadioBtn.click()

# hitting search
# TODO: a chance to practice OO programming here
search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()

# checking... hopefully Bama doesn't change their titles
print(driver.title)
# WebDriverWait(driver, 600)

# checking...
bamaState = Select(driver.find_element_by_id("p_state"))
#print([state.text for state in bamaState.options])

# look at the wheel go
# TODO: not mess around...
for state in bamaState.options:
    bamaState.select_by_visible_text(state.text)
    WebDriverWait(driver, 60)

driver.quit()

#inputElement = driver.find_element_by_name("q")
#inputElement.send_keys("cheese!")
#inputElement.submit()

#try:
    #WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    #WebDriverWait(driver, 60)
    #print(driver.title)

#finally:
    #driver.quit()
"""
