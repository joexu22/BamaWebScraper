import unittest
from bs4 import BeautifulSoup

class TestBeautifulSoup(unittest.TestCase):
    
    def test_parse(self):
        example_html = "<p>Hello World</p>"
        parsed_soup = BeautifulSoup(example_html, 'html.parser')
        parsed_soup_as_string = str(parsed_soup)
        self.assertEqual(parsed_soup_as_string, example_html)

if __name__ == '__main__':
    unittest.main()