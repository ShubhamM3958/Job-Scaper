import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs(job_title, location, num_pages=1):
    base_url = "https://www.linkedin.com/jobs/search/"
    jobs = []
    params = {
        'keywords': job_title,
        'location': location,
    }
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    for job in soup.findAll('div', class_='job-search-card'):
        url = job.find('a', class_='base-card__full-link')['href'].replace('https://in.', 'https://')
        title = job.find('h3', class_='base-search-card__title').text.strip()
        location = job.find('span', class_='job-search-card__location').text.strip()
        company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        jobs.append({'Title': title, 'Url': url, 'Location': location, 'Company': company})
    return pd.DataFrame(jobs)
