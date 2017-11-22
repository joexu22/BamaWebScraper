from bs4 import BeautifulSoup

with open("ecologicalpyramid.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')

#finding the first "primary consumer" in the list
primary_consumers = soup.find(id="primaryconsumers")
print(primary_consumers.li.div.string)

#using fuctions as soup
def is_secondary_consumer(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'
secondary_consumer = soup.find(is_secondary_consumer)
print(secondary_consumer.li.div.string)
