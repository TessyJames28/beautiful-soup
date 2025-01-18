from bs4 import BeautifulSoup
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


# Select (CSS selector) BeautifulSoup mimics the CSS styling
content = soup.select("p")
content1 = soup.select("div p") # grab all p tags inside a div tag
content2 = soup.select("h2 ~ p") # grab all p tags that are siblings of h2 tags
print(content2)