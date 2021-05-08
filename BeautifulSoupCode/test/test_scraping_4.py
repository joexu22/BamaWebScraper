import re
import unittest
from bs4 import BeautifulSoup

"""
Beautiful Soup and Regex Expressions...
"""

class TestBeautifulSoup(unittest.TestCase):
    def test_regex(self):
        with open('./html_folder/email_id.html') as email_id_example:
            soup = BeautifulSoup(email_id_example,"html.parser")

            # print(soup.prettify()) # what the html looks like

            # \w+ is one or more alphanumeric character
            email_id_regex = re.compile("\w+@\w+.\w+")

            # find the first item found by regex
            first_email_id = soup.find(text=email_id_regex)
            self.assertEqual(str(first_email_id).strip(), 'abc@example.com') # newlines and tabs need to be stripped

            # using find_all()
            email_ids = soup.find_all(text=email_id_regex)
            self.assertEqual(str(email_ids[0]).strip(), 'abc@example.com')
            self.assertEqual(str(email_ids[1]), 'xyz@example.com')
            self.assertEqual(str(email_ids[2]), 'foo@example.com')

            # using 'limit' to find the first two/"limit=2"
            email_ids_limited = soup.find_all(text=email_id_regex,limit=2)
            self.assertEqual(str(email_ids_limited[0]).strip(), 'abc@example.com')
            self.assertEqual(str(email_ids_limited[1]), 'xyz@example.com')

if __name__ == '__main__':
    unittest.main()

