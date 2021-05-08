from pathlib import Path
from random import randint
from selenium import webdriver

# No idea what the difference...
use_path = False
if (randint(0,1)==1 | use_path):
    path = Path(__file__).parent / "../Drivers/"
    browser = webdriver.Firefox(path)
else:
    browser = webdriver.Firefox()

browser.get('http://selenium.dev/')