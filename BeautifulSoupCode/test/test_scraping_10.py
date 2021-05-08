import unittest
from bs4 import BeautifulSoup

"""
Searching with regards to relations
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_find_and_search(self):

        with open('./html_folder/ecological_pyramid.html') as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        primaryconsumers = soup.find_all(class_="primaryconsumerlist")
        primaryconsumer = primaryconsumers[0]
        parent_ul = primaryconsumer.find_parents('ul')
        self.assertEqual(parent_ul[0].li.div.string, 'deer')

if __name__ == '__main__':
    unittest.main()