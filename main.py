import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString

def get_minor_sites():
    page = requests.get('http://catalog.illinois.edu/undergraduate/minors/')
    soup = BeautifulSoup(page.content, 'lxml')
    sites = []
    base_url = "http://catalog.illinois.edu"
    table = soup.find("div", {"id": "textcontainer"})
    for rows in table:
        if isinstance(rows, NavigableString):
            continue
        else:
            items = rows.findAll("li")
            for item in items:
                url = base_url + item.a.get("href")
                subpage = requests.get(url)
                content = BeautifulSoup(subpage.content, 'html5lib')
                lambda tag: tag.name == 'div' and tag.get('class') == ['info-section']
                links = content.find(lambda tag: tag.name == 'div' and (tag.get('id') == 'minortextcontainer' or tag.get('id') == 'minorstextcontainer'))
                if links is not None:
                    for link in links:
                        if isinstance(link, NavigableString):
                            continue
                        else:
                            titles = link.findAll('a', href=True)
                            for title in titles:
                                if "Minor in " in title.text:
                                    tup = ()
                                    tup = tup + (title.text[title.text.find("Minor in ") + len("Minor in "):].replace("\xa0", " "),)
                                    tup = tup + (base_url + title.get("href"),)
                                    sites.append(tup)
                                elif " Minor" in title.text:
                                    tup = ()
                                    tup = tup + (title.text[:title.text.find(" Minor") + len(" Minor")].replace("\xa0", " "),)
                                    tup = tup + (base_url + title.get("href"),)
                                    sites.append(tup)
                else:
                    tup = ()
                    tup = tup + (item.find('a').text,)
                    tup = tup + (url,)
                    sites.append(tup)
    return sites

def is_course_row(css_class):
    return css_class == "even" or css_class == "odd"

def getCredit(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    search_result = soup.find("div", class_="searchresult").h2.getText()
    return search_result[search_result.find("credit: ") + len("credit: ")]

def get_course_requirements(site):
    courses = []
    page = requests.get(site[1]).text
    soup = BeautifulSoup(page, 'html.parser')
    tables = soup.findAll("table", class_="sc_courselist")
    for table in tables:
            rows = table.findAll("tr", class_=is_course_row)
            for row in rows:
                req = ()
                cols = row.findAll("td", class_="codecol")
                base_url = "http://catalog.illinois.edu"
                for i, col in enumerate(cols):
                    req = req + (site[0],)
                    req = req + (col.getText().replace("\xa0", " "),)
                    url = base_url + col.a.get("href")
                    req = req + (getCredit(url),)
                cols = row.findAll("td", class_=None)
                for i, col in enumerate(cols):
                    req = req + (col.getText(),)
                if len(req) == 4:
                    courses.append(req)
    return courses

list = []
sites = get_minor_sites()
for i, site in enumerate(sites):
    req = get_course_requirements(site)
    if req is not None:
        list.append(req)
print(list)