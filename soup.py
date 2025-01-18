from bs4 import BeautifulSoup
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
print(header)