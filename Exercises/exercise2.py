from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

# Scrape and put the table content in Pandas Dataframe
url = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = BeautifulSoup(url.content, 'lxml')

# Locate the table in the webpage
table = soup.find("table")

# Extract the table headers
headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())
print(f"Headers: {headers}")
print("")

# Extract the table rows
rows = []
for tr in table.find_all("tr")[1:]:
    cells = tr.find_all('td')
    rows.append([cell.text.strip() for cell in cells])
print(f"Rows: {rows}")
print("")

# Create a pandas dataframe
df = pd.DataFrame(rows, columns=headers)

# Display the dataframe
print(df)
