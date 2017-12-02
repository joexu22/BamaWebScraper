# selenium files
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# sqlite3 files
import sqlite3
import sys

# TODO: solve the problem using multiple levels of webscraping, 1st level,
# 2nd level, etc. - aka breath first search levels


class bamaWebCrawler(object):
    """ Object Oriented class to aid in navigation of Bama's course
    equivalency website

    Attributes:
        TODO: Having it inherit from a object with a selection of webdrivers
        driver: A hands off browser, using Chrome
    """

    # TODO: The can be written in a config file
    # TODO: The website location can itself be scraped directly from google
    def __init__(self, driver_location="./chromedriver",
                 website_location="https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype"):
        self.driver_location = driver_location
        self.website_location = website_location
        self.driver = webdriver.Chrome("./chromedriver")

    def getToPickState(self):
        """ This function is reused to navigate towards the first branching
        operation. (TODO: Explore tree based solution)...
        """
        # initial starting website
        self.driver.get(self.website_location)

        # Selenium selections
        radio_button_css = "input[type='radio'][value='BAMANAME']"
        bamaRadioBtn = self.driver.find_element_by_css_selector(
            radio_button_css)
        bamaRadioBtn.click()
        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

    def pickStateSchool(self, state, school):
        """ navigates Bama's website with state and school
        hacking this... I'll refactor when the code acutally works :(
        """
        self.driver.get(self.website_location)

        radio_button_css = "input[type='radio'][value='BAMANAME']"
        bamaRadioBtn = self.driver.find_element_by_css_selector(
            radio_button_css)
        bamaRadioBtn.click()

        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

        stateList = Select(self.driver.find_element_by_id("p_state"))
        stateList.select_by_visible_text(state)

        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

        schoolList = Select(self.driver.find_element_by_id("p_sbgi"))
        schoolList.select_by_visible_text(school)

        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

        # Following this is an hack... will refactor
        #searchBox = self.driver.find_element_by_id("crse_name_input_id")
        #searchBox.send_keys("LOTS OF MEANINGLESS WORDS FOR ME")
        # WebDriverWait(self.driver,600)
        #search_button_css = "input[type='submit'][value='Get Course List']"
        #bamaSearchBtn = self.driver.find_element_by_css_selector(search_button_css)
        # bamaSearchBtn.click()

    def pickCourse(self, courseName):
        searchBox = self.driver.find_element_by_id("crse_name_input_id")
        searchBox.send_keys(courseName)
        search_button_css = "input[type='submit'][value='Get Course List']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

    def clickSearchButton(self):
        # TODO: refactor the clicking?
        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = self.driver.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

    def getStateList(self):
        """anciliary function for getting the list of States
        """
        self.getToPickState()
        # option list with all the US States
        stateList = Select(self.driver.find_element_by_id("p_state"))
        # logic...
        # stateList = [state.text for state in stateList.options]
        return stateList

    def selectSchool(self, stateName):
        """ TODO: Logic is busted here; this should be called selectSchool or
        getToSchoolList...
        """
        stateList = self.getStateList()
        stateList.select_by_visible_text(stateName)

    def getSchoolList(self):
        schoolList = Select(self.driver.find_element_by_id("p_sbgi"))
        schoolList = [school.text for school in schoolList.options]
        return schoolList

    def pauseWebdriver(self, time=100):
        WebDriverWait(self.driver, time)

    def closeBrowser(self):
        self.driver.quit()


def main():
    # __main__ program here
    dataCollector = bamaWebCrawler()

    # convert into array of text
    stateList = dataCollector.getStateList()
    stateList = [state.text for state in stateList.options]
    # print stateList

    # insert into DB
    connection = sqlite3.connect('bamaCourseTables.db')
    with connection:
        cursor = connection.cursor()

        # TODO: research proper database "non-scripting" solutions
        cursor.execute("DROP TABLE IF EXISTS States")
        cursor.execute("CREATE TABLE States(State TEXT PRIMARY KEY)")

        for state in stateList:
            cursor.execute("INSERT INTO States VALUES(?)", (state,))

# if __name__ == "__main__":
#     main()

# dataCollector = bamaWebCrawler()
# stateList = dataCollector.getStateList()
# stateList = [state.text for state in stateList.options]


def getAllSchoolNames():
    # hacking around "a problem"...
    connection = sqlite3.connect('bamaCourseTables.db')
    with connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Schools")
        cursor.execute("CREATE TABLE Schools(State TEXT, School TEXT)")

    # shortened test list
    stateList = ['Alabama', 'Massachusetts']

    for state in stateList:
        # heavy code (branching) here... may need headless drivers
        # TODO: implement parallism here
        newSchoolList = bamaWebCrawler()

        # getting the list of schools here from a state
        newSchoolList.selectSchool(state)
        newSchoolList.clickSearchButton()
        schoolList = newSchoolList.getSchoolList()

        # create another SQL table here
        connection = sqlite3.connect('bamaCourseTables.db')
        with connection:
            cursor = connection.cursor()

            for school in schoolList:
                cursor.execute(
                    "INSERT INTO Schools VALUES(?,?)", (state, school))

        # cleanup and concurrency issues
        newSchoolList.pauseWebdriver(250)
        newSchoolList.closeBrowser()


# access each item in database
# TODO: "eventually", get the list from the database
randomSchool = None
connection = sqlite3.connect('bamaCourseTables.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Schools")
    stateSchool = cursor.fetchall()
    import random
    randomSchool = random.choice(stateSchool)
    # making sure the data coming out are tuples
    # for entry in stateSchool:
    #    print entry
print randomSchool

# Test Setup... Need to set up test driven development...
# script getting too big
randomSchool = (u'Massachusetts', u'Univ of Massachusetts Lowell')
print randomSchool[0]
print randomSchool[1]

courseSearch = bamaWebCrawler()
courseSearch.pickStateSchool(randomSchool[0], randomSchool[1])
# picking everything
# courseSearch.pickCourse("%")


# for state in stateList:
# very heavy code here... may need headless drivers
# bamaState.select_by_visible_text(state)

"""
search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = driver.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()
"""

"""
for state in bamaState.options:
    bamaState.select_by_visible_text(state.text)
    WebDriverWait(driver, 60)
"""

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

# pickState()


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
