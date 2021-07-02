from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# connect to webdriver
browser = webdriver.Firefox()
browser.get('https://ssb.ua.edu/pls/PROD/rtstreq.P_Searchtype')

print(browser.title)

# selecting radio-button
radio_button_css = "input[type='radio'][value='BAMANAME']"
bamaRadioBtn = browser.find_element_by_css_selector(radio_button_css)
bamaRadioBtn.click()

# hitting search
# TODO: a chance to practice OO programming here
search_button_css = "input[type='submit'][value='Submit']"
bamaSearchBtn = browser.find_element_by_css_selector(search_button_css)
bamaSearchBtn.click()

# checking... hopefully Bama doesn't change their titles
print(browser.title)
WebDriverWait(browser, 600)

# checking...
bamaState = Select(browser.find_element_by_id("p_state"))
#print([state.text for state in bamaState.options])

# look at the wheel go
# TODO: not mess around...
for state in bamaState.options:
    bamaState.select_by_visible_text(state.text)
    WebDriverWait(browser, 60)

browser.quit()
#inputElement = driver.find_element_by_name("q")
#inputElement.send_keys("cheese!")
#inputElement.submit()

#try:
    #WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    #WebDriverWait(driver, 60)
    #print(driver.title)

#finally:
    #driver.quit()
