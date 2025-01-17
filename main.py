from bs4 import BeautifulSoup
import requests
from filter import filter
import time
# Scrap a website to get all jobs that requires python skills

# Filter based on user skills
print("==============Enter skill you want to filter out, separated by coma==============")
unfamiliar_skills = input("> ").split(',')
print(f"Filtering out {unfamiliar_skills}...")


def find_jobs():
    url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text

    # Search and grab elements from the website
    soup = BeautifulSoup(url, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        # Remove excess spaces and normalize the skills 
        skills = job.find('div', class_ = 'more-skills-sections').text.strip() # Remove spaces
        skills = (' ').join(skills.split()).lower()
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip() # Remove spaces       
        job_link = job.header.h2.a['href']  # Get the job link
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if "1" or "2" or "few" in published_date:
            if filter(unfamiliar_skills, skills):
                print(f"Company Name: {company_name}")
                print(f"Required Skills: {skills}")
                print(f"Job Link: {job_link}")
                print("")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 15
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)  # 90 minutes
