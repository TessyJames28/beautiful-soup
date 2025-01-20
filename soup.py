from bs4 import BeautifulSoup, NavigableString, Comment
import re # Regular expression
import requests

# Load webpage content
url = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# Convert to a beautiful soup object
soup = BeautifulSoup(url.content, 'lxml')
# print(soup.prettify()) # Print the content of the webpage

# Find the first header in the webpage
first_header = soup.find("h2") # Find the first header in the webpage
first_headers = soup.find_all("h2") # Find all headers in the webpage

headers = soup.find_all(["h1", "h2"]) # Find all headers in the webpage passed as list
# print(headers)

# Pass in attributes to the find/find_all function
# Use attrs to pass in a dictionary of attributes
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})

# Nesting find/find_all calls
body = soup.find("body")
div = body.find("div")
header = div.find("h1")

# Search for specific strings in the find/find_all call using regex
string_search = soup.find_all("p", string=re.compile("Some"))
headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
# print(f"Headers: {headers}")

# Select (CSS selector) BeautifulSoup mimics the CSS styling
content = soup.select("p")
content1 = soup.select("div p") # grab all p tags inside a div tag
content2 = soup.select("h2 ~ p") # grab all p tags that are siblings of h2 tags

# Grab specific elements with id selector
bold = soup.select("p#paragraph-id b")

# Run nested calls
paragraphs = soup.select("body > p") # Direct child of the  body tag
# print(paragraphs)
# Loop through the the list of elements and print them
for paragraph in paragraphs:
    print(paragraph.select("i")) # Select all italic tags inside the paragraph


# Getting different properties of the HTML
# Get the string of the tag using .string
header = soup.find("h2")
# print(header.string)

# Using get_text() method to get the text with multiple child elements
div = soup.find("div")
# print(div.get_text())

# Get a specific property from an element
link = soup.find("a")
# print(link['href']) # Get the href attribute of the a tag

paragraphs = soup.select("p#paragraph-id")
# print(paragraphs[0]["id"]) # Get the id attribute of the p tag


# Path syntax
# print(soup.body.div) # Get the first div tag inside the body tag
# print(soup.body.div.h1) # Get the first h1 tag inside the div tag inside the body tag
# print(soup.body.div.h1.string) # Get the string of the h1 tag inside the div tag inside the body tag


# Paraent, sibling, and child
# print(soup.body.prettify())
div = soup.body.find("div")
next_sibling = div.find_next_siblings()
print(next_sibling)
