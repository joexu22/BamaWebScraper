import unittest
from bs4 import BeautifulSoup
from pathlib import Path

"""
Understanding how HTML Tags work
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_tags(self):
        path = Path(__file__).parent / "../html_folder/a_tag.html"
        with open(path) as a_tag_html:
            soup = BeautifulSoup(a_tag_html, 'html.parser')

            # how the tagging works
            a_tag = soup.a
            self.assertEqual(str(a_tag), '<a href="http://www.packtpub.com">Home</a>')
            self.assertEqual(str(type(soup)), "<class 'bs4.BeautifulSoup'>")
            self.assertEqual(a_tag.attrs, {'href': 'http://www.packtpub.com'})
            self.assertEqual(a_tag.attrs['href'], 'http://www.packtpub.com')

            # changing a tag while it is a soup object
            a_tag.name = 'p'
            self.assertEqual(str(a_tag), '<p href="http://www.packtpub.com">Home</p>')

            # first tag detected
            self.assertEqual(str(soup.p), '<p>Test html a tag example</p>')

            # first element detected
            self.assertEqual(str(a_tag['href']), 'http://www.packtpub.com')

if __name__ == '__main__':
    unittest.main()

