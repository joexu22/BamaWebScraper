from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Creating a instance of Chrome driver
driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.google.com")
print(driver.title)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("cheese!")
inputElement.submit()

try:
    #WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    WebDriverWait(driver, 10)
    print(driver.title)

finally:
    driver.quit()
