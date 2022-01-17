import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

7


def get_jobs(html):
    result = requests.get(html, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    pool = soup.find("table", {"id": "jobsboard"})

    title = pool.find_all("h2", {"itemprop": "title"})
    company = pool.find_all("h3", {"itemprop": "name"})
    link = pool.find_all("a", {"itemprop": "url"})

    jobs = []
    for n in range(len(title)):
        jobs.append({
            'title': title[n].string,
            'company': company[n].string,
            'location': "Likely WorldWide",
            "apply_link": "https://remoteok.com/"+link[n]["href"]
        })

    return(jobs)

def get_remoteok_jobs(word):
  print("Scrapping remoteok jobs ...")
  URL = f"https://remoteok.com/remote-{word}-jobs?hide_sticky=&compact_mode=&location=worldwide"
  return get_jobs(URL)