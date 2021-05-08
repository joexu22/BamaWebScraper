import unittest
from bs4 import BeautifulSoup

class TestBeautifulSoup(unittest.TestCase):
    def test_find(self):
        
        with open("./html_folder/ecological_pyramid.html") as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        # finding the first item in an "unordered list"
        producer_entries = soup.find('ul')
        self.assertEqual(str(producer_entries.li.div.string), 'plants')

        # find() method in BeautifulSoup
        # find(name,attrs,recursive,text,**kwargs)

        # finding soup.find(name = "li")
        tag_li = soup.find("li")
        self.assertEqual(str(type(tag_li)), "<class 'bs4.element.Tag'>")

        # searching for text in soup object
        search_for_stringonly = soup.find(text="fox")
        self.assertEqual(str(search_for_stringonly), 'fox')

        # note about being case sensitive
        case_sensitive_string = soup.find(text="Fox")
        # will return None
        self.assertEqual(case_sensitive_string, None)
        self.assertNotEqual(str(case_sensitive_string), 'Fox')

if __name__ == '__main__':
    unittest.main()
