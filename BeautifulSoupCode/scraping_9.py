from bs4 import BeautifulSoup

with open('ecologicalpyramid.html','r') as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, 'lxml')

all_texts = soup.find_all(text=True)
print(all_texts)
print

all_texts_in_list = soup.find_all(text=["plants","algae"])
print(all_texts_in_list)
print

div_li_tags = soup.find_all(['div','li'])
print(div_li_tags)
print

all_css_class = soup.find_all(class_ = ["producerlist","primaryconsumerlist"])
print(all_css_class)
print(all_css_class[0])
print(all_css_class[1])
print(all_css_class[2])
print(all_css_class[3])
