import requests
from bs4 import BeautifulSoup

def get_wework_jobs(word):
    URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    result = soup.find("div", {"class": "jobs-container"}).find_all("a")
    print("Scrapping wework jobs ...")
    jobs=[]
    for item in result:
        href = item.get("href")
        if (href != None) and ("/remote-jobs/" in href):
            link = f"https://weworkremotely.com/{href}"
            company = item.find("span", {"class", "company"}).string
            title = item.find("span", {"class", "title"}).string
            location = item.find("span", {"class", "region company"})
            if location is None:
                location = "N/A"
            else:
                location = location.string
            jobs.append({
            'title': title,
            'company': company,
            'location': location,
            "apply_link": link
            })
    return jobs
