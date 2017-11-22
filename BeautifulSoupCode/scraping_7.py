import re
from bs4 import BeautifulSoup

"""
Using Combinations in Find()
"""

identical_example = """<p class="identical">
Example of p tag with class identical
</p>
<div class="identical">
Example of div tag with class identical
</div>
"""
soup = BeautifulSoup(identical_example,"lxml")
identical_div = soup.find("div", class_ = "identical")
print(identical_div)
