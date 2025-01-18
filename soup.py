from bs4 import BeautifulSoup
import requests

# Load webpage content
url = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# Convert to a beautiful soup object
soup = BeautifulSoup(url.content)
print(soup.prettify()) # Print the content of the webpage