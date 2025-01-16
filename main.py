from bs4 import BeautifulSoup
import requests
# Scrap a website to get all jobs that requires python skills

url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text

# Search and grab elements from the website
soup = BeautifulSoup(url, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') # Remove spaces
skills = job.find('div', class_ = 'more-skills-sections').text.replace(' ', '') # Remove spaces               
print(skills)