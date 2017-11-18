from bs4 import BeautifulSoup
import urllib

markup = urllib.urlopen('http://xuguanzhou.com').read()
soup = BeautifulSoup(markup,"lxml")
print type(soup)

print soup.prettify()
#with open("index.html") as fp:
#    soup = BeautifulSoup(fp)
#soup = BeautifulSoup("<html>data</html>")

#print(soup.prettify())
