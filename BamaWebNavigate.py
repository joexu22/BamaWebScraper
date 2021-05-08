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
from sqlite3 import Error

# beautiful soup
from bs4 import BeautifulSoup
import re

# config
import configparser

# TODO: make this file an importable class file

# headless display
# display = Display(visible=0, size=(800,600))
display = Display(visible=0)
display.start()

Config = configparser.ConfigParser()
Config.read(sys.path[0] + "/config.conf")

driver_location = Config.get('default', 'driver_location')
website_location = Config.get('default', 'website_location')
database_location = Config.get('default', 'database_location')


def getEntryFromDB():
    try:
        connection = sqlite3.connect(sys.path[0] + database_location)
    except Error as e:
        print(e)
        sys.exit()

    # get the tuples from the database
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Schools")
        return cursor.fetchall()


def hasEquivalentCourse(state, school):

    # TODO: switch statement allowing for any webdriver
    driver = webdriver.Chrome(sys.path[0] + driver_location)
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
    soup = BeautifulSoup(html_page, 'html.parser')

    # TODO: some smart string parsing algorithm here
    class_regexp_1 = re.compile(".*Formal.*")
    class_regexp_2 = re.compile(".*Algori.*")

    target_class_1 = soup.find_all(text=class_regexp_1)
    target_class_2 = soup.find_all(text=class_regexp_2)
    target_class = target_class_1 + target_class_2

    # TODO: potentially remove duplicates here
    # TODO: this need to be make optional; filter out non CS470 or CS475
    # TODO: code golf oppurtunity...
    equi_classes = []
    for target in target_class:
        if (target.parent.parent.find_all(text="470")
                or target.parent.parent.find_all(text="475")):
            equi_classes.append(target)

    if not equi_classes:
        driver.close()
        return 0
    else:
        # for target_equivalency in target_class:
        for target_equivalency in equi_classes:
            try:
                target_school = open("targetSchools.html", "a")
                # formatting it into table
                target_school.write("<tr>\n")
                target_school.write("<td>State</td>\n")
                target_school.write("<td>" + state + "</td>\n")
                target_school.write("<td>School</td>\n")
                target_school.write("<td>" + school + "</td>\n")
                target_school.write("</tr>\n")
                target_school.write(str(target_equivalency.parent.parent))
                target_school.close()
            except AttributeError:
                # some error that I'm not expecting
                pass

    # clean-up
    driver.close()


if __name__ == "__main__":
    # nuking file
    f = open("targetSchools.html", "w")
    file_heading = """
    <!DOCTYPE html>
    <html>
    <body>
    <table style="width:100%">
    """
    f.write(file_heading)
    f.close()
    stateSchool = getEntryFromDB()
    stateSchool = [(u'Massachusetts', u'Univ of Massachusetts Lowell'),
                   (u'Alabama', u'Auburn University Main Campus')]
    # stateSchool = [(u'Oregon', u'Oregon State University'),(u'Alabama', u'Alabama State University')]
    # stateSchool = [(u'Alabama', u'Alabama State University')]
    for entry in stateSchool:
        # print entry[0] + " " + entry[1]
        hasEquivalentCourse(entry[0], entry[1])
    f = open("targetSchools.html", "a")
    file_footing = """
    </table>
    </body>
    </html>
    """
    f.write(file_footing)
    f.close()
