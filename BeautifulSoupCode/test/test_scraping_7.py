import unittest
from bs4 import BeautifulSoup
from pathlib import Path

"""
Using Combinations in Find()
e.g. combining "div" & class_ 
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_combination(self):
        path = Path(__file__).parent / "../html_folder/identical_tag.html"
        with open(path) as html:
            soup = BeautifulSoup(html, "html.parser")
        
        identical_div = soup.find("div", class_ = "identical")
        text_div = '<div class="identical"> Example of div tag with class identical </div>'
        self.assertEqual(str(identical_div), text_div)

        identical_p = soup.find("p", class_ = "identical")
        text_p = '<p class="identical"> Example of p tag with class identical </p>'
        self.assertEqual(str(identical_p), text_p)

if __name__ == '__main__':
    unittest.main()


