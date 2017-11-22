from bs4 import BeautifulSoup

"""
Searching with regards to relations
"""

with open('ecologicalpyramid.html','r') as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')

primaryconsumers = soup.find_all(class_="primaryconsumerlist")
primaryconsumer = primaryconsumers[0]
parent_ul = primaryconsumer.find_parents('ul')
print(parent_ul)
