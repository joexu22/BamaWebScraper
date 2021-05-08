import unittest
from bs4 import BeautifulSoup

"""
Using find_all()
"""
class TestBeautifulSoup(unittest.TestCase):
    def test_find_all(self):

        with open('./html_folder/ecological_pyramid.html') as ecological_pyramid:
            soup = BeautifulSoup(ecological_pyramid, 'html.parser')

        # using find_all()
        all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerlist")

        # expected list
        expected_list = ['lion', 'tiger']

        # iteration of list
        for x in range(len(expected_list)):
            self.assertEqual(expected_list[x], all_tertiaryconsumers[x].div.string)

if __name__ == '__main__':
    unittest.main()