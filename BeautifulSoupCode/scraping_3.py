from bs4 import BeautifulSoup

with open("ecologicalpyramid.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')

#finding the first item in an "unordered list"
producer_entries = soup.find('ul')
print(producer_entries.li.div.string)

#find() method in BeautifulSoup
#find(name,attrs,recursive,text,**kwargs)

#finding soup.find(name = "li")
tag_li = soup.find("li")
print(type(tag_li))

#searching for text in soup object
search_for_stringonly = soup.find(text="fox")
print(search_for_stringonly)
#note about being Case Sensitive
case_sensative_string = soup.find(text="Fox")
#will return None
print(case_sensative_string)
