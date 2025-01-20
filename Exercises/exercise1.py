from bs4 import BeautifulSoup
import requests
import re

# Grab all of the social links from the webpage in 3 different ways
# Should use at least 1 find/find_all and 1 select method
url = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = BeautifulSoup(url.content, 'lxml')
# print(soup.prettify())

# Using Find_all method
socials = soup.find_all("ul", attrs = {"class": "socials"})
for social in socials:
    link = social.find_all("li")
    print("Using find_all method")
    for l in link:
        print(l.a["href"])

# Using regex with find_all
socials = soup.find_all("li", attrs = {"class": re.compile("social")})
print("\nUsing regex with find_all")
for social in socials:
    print(social.a["href"])


# Using select method
socials = soup.select("ul.socials")
print("\nUsing select method")
for social in socials:
    links = social.select("li")
    for link in links:
        print(link.a["href"])
