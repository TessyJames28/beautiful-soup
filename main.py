from bs4 import BeautifulSoup
import requests
# Scrap a website to get all jobs that requires python skills

url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text

# Search and grab elements from the website
soup = BeautifulSoup(url, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if "1" or "2" or "few" in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip() # Remove spaces
        skills = job.find('div', class_ = 'more-skills-sections').text.strip() # Remove spaces
        skills = (' ').join(skills.split()) # Remove excess spaces and normalize the skills        
        print(f"""
        Company Name: {company_name}
        Required Skills: {skills}
        """)
        print('')