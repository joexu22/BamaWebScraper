import unittest
from bs4 import BeautifulSoup
from pathlib import Path

class TestBeautifulSoup(unittest.TestCase):
    def test_soup_functions(self):
        path = Path(__file__).parent / "../html_folder/ecological_pyramid.html"
        with open(path) as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        # finding the first "primary consumer" in the list
        primary_consumers = soup.find(id="primaryconsumers")
        self.assertEqual(str(primary_consumers.li.div.string), 'deer')

        # using functions with soup
        # the function does not seem to need any parameters passed to it
        def is_secondary_consumer(tag):
            return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'
        secondary_consumer = soup.find(is_secondary_consumer)
        #print(type(secondary_consumer))
        self.assertEqual(str(secondary_consumer.li.div.string), 'fox')

if __name__ == '__main__':
    unittest.main()