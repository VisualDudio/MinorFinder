import requests
from bs4 import BeautifulSoup

def get_sites():
    page = requests.get('http://catalog.illinois.edu/undergraduate/minors/')
    soup = BeautifulSoup(page.content, 'html.parser')
    sites = []
    base_url = "http://catalog.illinois.edu"
    table = soup.findAll("div", {"class": "tab_content"})
    for rows in table:
        items = rows.findAll("li")
        for item in items:
            sites.append(base_url + item.a.get("href"))
    return sites