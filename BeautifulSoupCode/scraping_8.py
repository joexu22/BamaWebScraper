from bs4 import BeautifulSoup

with open('ecologicalpyramid.html','r') as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')

#using find_all()
all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")
print(type(all_tertiaryconsumers))
print("")

#iteration of list
for tertiaryconsumer in all_tertiaryconsumers:
    print(tertiaryconsumer.div.string)
