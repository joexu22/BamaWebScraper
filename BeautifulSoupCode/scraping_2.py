import urllib2
from bs4 import BeautifulSoup

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.packtpub.com'>Home</a>
<a href="http;//www.packtpub.com/books'>Books</a>
</body>
</html>"""

soup = BeautifulSoup(html_atag,'lxml')
atag = soup.a

#print(atag)
#print(type(atag))
#print(atag.attrs)
tag_name = atag.name
print(tag_name)

print("")
#changing the tag name while it's a soup object
atag.name = 'p'
print(soup)

#learning tags...
print("")
atag = soup.tag
#print(atag['href'])
#first_a_string = soup.
