import urllib2
from bs4 import BeautifulSoup

"""
url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_packtpage = BeautifulSoup(page, 'lxml')
"""

helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, 'xml')
print(soup_string)

#output_file = open('workfile.txt', 'w')
#output_file.write("Testing/Testing\n")

#with open("foo.html","r") as foo_file:
#    soup_foo = BeautifulSoup(foo_file)
