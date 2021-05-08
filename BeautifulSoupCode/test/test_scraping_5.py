import unittest
from bs4 import BeautifulSoup

class TestBeautifulSoup(unittest.TestCase):
    def test_soup_functions(self):
        with open("./html_folder/ecological_pyramid.html", "r") as ecological_pyramid:
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