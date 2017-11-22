import re
from bs4 import BeautifulSoup

"""
HTML5 Custom Attributes
"""

customattr = """<p data-custom="custom">custom attribute example</p>"""
customsoup = BeautifulSoup(customattr,'lxml')
#this would be an expected error
#customSoup.find(data-custom="custom")

#dictionary structure useful when variable is in conflict
#hyphenated words, keywords, etc.
using_attrs = customsoup.find(attrs={'data-custom':'custom'})
print(using_attrs)
print("")

with open("ecologicalpyramid.html","r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')
using_class = soup.find(attrs={"class":"primaryconsumerlist"})
print(using_class)
print("")

#special "class_" keyword
using_class_ = soup.find(class_ = "primaryconsumerlist")
print(using_class_)
