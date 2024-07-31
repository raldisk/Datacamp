# 1/2
from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector(text=html)

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath("//div")

# 2/2
# The code len( divs[2].xpath('./*') ) gives the total number of children of the third div element in the HTML code.
