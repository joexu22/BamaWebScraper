import unittest
from bs4 import BeautifulSoup
from pathlib import Path

"""
Specific Find and Search
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_find_and_search(self):

        path = Path(__file__).parent / "../html_folder/ecological_pyramid.html"
        with open(path) as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        # the html is tokenized as an array of texts
        all_texts = soup.find_all(text=True)
        all_texts_filtered = [i for i in all_texts if '\n' not in i]
        expected_text = ['plants', '100000', 'algae', '100000', 'deer', '1000', 'rabbit', '2000', 'fox', '100', 'bear', '100', 'lion', '80', 'tiger', '50']
        self.assertEqual(all_texts_filtered, expected_text)

        # search for specific text
        all_texts_in_list = soup.find_all(text=["plants","algae"])
        expected_text = ["plants","algae"]
        self.assertEqual(all_texts_in_list, expected_text)

        # find all 'tags'
        div_li_tags = soup.find_all(['div','li'])
        for item in div_li_tags:
            # print(item) # lots to parse
            # print(type(item))
            self.assertEqual(str(type(item)), "<class 'bs4.element.Tag'>")

        # find particular classes
        all_css_class = soup.find_all(class_ = ["producerlist","primaryconsumerlist"])
        self.assertEqual(all_css_class[0].div.string, 'plants')
        self.assertEqual(all_css_class[1].div.string, 'algae')
        self.assertEqual(all_css_class[2].div.string, 'deer')
        self.assertEqual(all_css_class[3].div.string, 'rabbit')

if __name__ == '__main__':
    unittest.main()
