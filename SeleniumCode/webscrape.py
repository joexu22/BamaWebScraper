from bs4 import BeautifulSoup
import requests

"""
get the html for my personal website
"""

markup = requests.get('http://xuguanzhou.com')

soup = BeautifulSoup(markup.text,"html.parser")
print(type(soup))
print(soup.prettify())
