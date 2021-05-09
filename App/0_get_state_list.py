# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""
This script will scrape all the schools that The University of Alabama
recognizes in regards to course equivalency
"""

# Global Environment Variable
WEBSITE_LOCATION = 'https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype'

"""
Gets the list of US States
"""
def getStateList():
    # start webdriver and get website location
    dataCollector = webdriver.Firefox()
    dataCollector.get(WEBSITE_LOCATION)

    # navigate and retrieve website location
    # step 1 - select radio button
    radio_button_css = "input[type='radio'][value='BAMANAME']"
    bamaRadioBtn = dataCollector.find_element_by_css_selector(radio_button_css)
    bamaRadioBtn.click()
    # step 2 - click submit
    search_button_css = "input[type='submit'][value='Submit']"
    bamaSearchBtn = dataCollector.find_element_by_css_selector(search_button_css)
    bamaSearchBtn.click()

    # scrapes
    stateList = Select(dataCollector.find_element_by_id("p_state"))
    stateList = [state.text for state in stateList.options]

    #cleanup
    dataCollector.quit()
    return stateList

if __name__ == '__main__':
    states = getStateList()
    print(states)
    print("Number Of 'States': ", len(states))
