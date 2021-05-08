import unittest
from bs4 import BeautifulSoup
from pathlib import Path

"""
HTML5 Custom Attributes
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_custom_attributes(self):

        custom_attr = """<p data-custom="custom">custom attribute example</p>"""
        custom_soup = BeautifulSoup(custom_attr,'html.parser')

        # this would be an expected error
        # customSoup.find(data-custom="custom")

        # dictionary structure useful when variable is in conflict
        # hyphenated words, keywords, etc.
        using_attrs = custom_soup.find(attrs={'data-custom':'custom'})
        self.assertEqual(str(using_attrs),'<p data-custom="custom">custom attribute example</p>')

        path = Path(__file__).parent / "../html_folder/ecological_pyramid.html"
        with open(path) as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        # find 'class' attribute
        using_class = soup.find_all(attrs={"class":"primaryconsumerlist"})
        self.assertEqual(str(using_class[0].div.string), 'deer')
        self.assertEqual(str(using_class[1].div.string), 'rabbit')

        # special "class_" keyword
        using_class_ = soup.find_all(class_ = "primaryconsumerlist")
        self.assertEqual(str(using_class[0].div.string), 'deer')
        self.assertEqual(str(using_class[1].div.string), 'rabbit')

if __name__ == '__main__':
    unittest.main()
