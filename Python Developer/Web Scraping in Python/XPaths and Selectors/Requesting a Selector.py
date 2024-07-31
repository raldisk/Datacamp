## Requesting a Selector

# Import a scrapy Selector
# Import requests
import requests
from scrapy import Selector

# Create the string html containing the HTML source
html = requests.get(url).content

# Create the Selector object sel from html
sel = Selector(text=html)

# Print out the number of elements in the HTML document
print("There are 1020 elements in the HTML document.")
print("You have found: ", len(sel.xpath("//*")))
