from bs4 import BeautifulSoup
import requests
import re

# Grab fun fact with that contains the word "is"
url = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = BeautifulSoup(url.content, 'lxml')

# Using the find/find_all method
fun_facts = soup.find("ul", attrs = {"class": "fun-facts"})
print("Using find method:")
facts = fun_facts.find_all("li")
for fact in facts:
    if "is" in fact.text:
        print(fact.text)


# Using the select method with regex
print("\nUsing select method with regex:")
fun_facts = soup.select("ul.fun-facts li")
for fact in fun_facts:
    if re.search(r"is", fact.text):
        print(fact.text)