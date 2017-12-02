# selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# sqlite3
import sqlite3
import sys

# config
import configparser

# headless
from pyvirtualdisplay import Display

"""
This script is meant to generate a database containing all the colleges and
universities that Bama recognizes in regards to course equivalency
"""
Config = configparser.ConfigParser()
Config.read(sys.path[0] + "/config.conf")

driver_location = Config.get('default', 'driver_location')
website_location = Config.get('default', 'website_location')

def getStateList():
    # start webdriver and get website location
    display = Display(visible=0)
    display.start()
    dataCollector = webdriver.Chrome(sys.path[0]+driver_location)
    dataCollector.get(website_location)

    # navigate and retrieve website location
    radio_button_css = "input[type='radio'][value='BAMANAME']"
    bamaRadioBtn = dataCollector.find_element_by_css_selector(
        radio_button_css)
    bamaRadioBtn.click()
    search_button_css = "input[type='submit'][value='Submit']"
    bamaSearchBtn = dataCollector.find_element_by_css_selector(
        search_button_css)
    bamaSearchBtn.click()
    stateList = Select(dataCollector.find_element_by_id("p_state"))
    stateList = [state.text for state in stateList.options]

    #cleanup
    dataCollector.quit()
    display.stop()
    return stateList

def getAllSchoolNames(stateList):
    """
    this is a short script that is somewhat reliant on the stability of
    Bama's site
    """

    # good for testing and ensuring newest tables
    connection = sqlite3.connect('bamaCourseTables.db')
    with connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Schools")
        cursor.execute("CREATE TABLE Schools(State TEXT, School TEXT)")

    # TODO: refactor once everything works

    # here enables headless implementation
    display = Display(visible=0)
    display.start()
    for state in stateList:
        dataCollector = webdriver.Chrome(sys.path[0]+driver_location)
        dataCollector.get(website_location)

        # navigate and retrieve website location
        radio_button_css = "input[type='radio'][value='BAMANAME']"
        bamaRadioBtn = dataCollector.find_element_by_css_selector(
            radio_button_css)
        bamaRadioBtn.click()

        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = dataCollector.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

        stateOptions = Select(dataCollector.find_element_by_id("p_state"))
        stateOptions.select_by_visible_text(state)

        search_button_css = "input[type='submit'][value='Submit']"
        bamaSearchBtn = dataCollector.find_element_by_css_selector(
            search_button_css)
        bamaSearchBtn.click()

        # able to get each school by school_list
        schoolList = Select(dataCollector.find_element_by_id("p_sbgi"))
        schoolList = [school.text for school in schoolList.options]

        # fast solutions call for dirty code...
        # create SQL table here
        connection = sqlite3.connect('bamaCourseTables.db')
        with connection:
            cursor = connection.cursor()

            for school in schoolList:
                cursor.execute(
                    "INSERT INTO Schools VALUES(?,?)", (state, school))

if __name__ == '__main__':
    states = getStateList()
    getAllSchoolNames(states)
