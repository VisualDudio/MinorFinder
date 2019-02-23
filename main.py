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


def is_course_row(css_class):
    return css_class == "even" or css_class == "odd"


def get_course_requirements(url):
    courses = []

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    tables = soup.findAll("table", class_="sc_courselist")
    for table in tables:
        rows = table.findAll("tr", class_=is_course_row)
        for row in rows:
            req = ()
            cols = row.findAll("td", class_="codecol")
            for i, col in enumerate(cols):
                req = req + (col.getText().replace("\xa0", ""),)
            cols = row.findAll("td", class_=None)
            for i, col in enumerate(cols):
                req = req + (col.getText(),)
            if len(req) == 2:
                courses.append(req)
    return courses


def getCredit (url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    search_result = soup.find("div", class_="searchresult").h2.getText()
    search_result = search_result[search_result.find("credit: ") + len("credit: ")]
    
    print(search_result)

url = "http://catalog.illinois.edu/search/?P=MATH%20347"
getCredit(url)
