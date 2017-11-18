import re
from bs4 import BeautifulSoup

"""
Beautiful and Regex Expressions...
"""

email_id_example = """<br/>
<div>The below HTML has the information that has email ids.</div>
abc@example.com
<div>xyz@example.com</div>
<span>foo@example.com</span>
"""
soup = BeautifulSoup(email_id_example,"lxml")
#\w+ is one or more alphanumeric character
emailid_regexp = re.compile("\w+@\w+.\w+")
first_email_id = soup.find(text=emailid_regexp)
print(first_email_id)
