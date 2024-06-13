from scrape_jobs import scrape_jobs
from visualize_jobs import visualize_jobs


def main():

    # job_title = "java internship"
    # location = "Delhi, India"
    job_title = input('Enter Job Title: ')
    location = input('Enter Location: ')
    job_data = scrape_jobs(job_title, location)
    job_data.drop_duplicates(inplace=True)
    print(job_data)

    visualize_jobs(job_data, location, job_title)


if __name__ == '__main__':
    main()

