import seaborn as sns
import matplotlib.pyplot as plt


def visualize_jobs(job_data, location, job_title):
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Company', data=job_data, order=job_data['Company'].value_counts().iloc[:10].index)
    plt.title(f'Top Companies Hiring for {job_title} in {location}')
    plt.xlabel('Number of Job Postings')
    plt.ylabel('Company')
    plt.show()