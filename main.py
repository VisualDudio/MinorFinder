import requests
from bs4 import BeautifulSoup


def get_minor_sites():
    page = requests.get('http://catalog.illinois.edu/undergraduate/minors/')
    soup = BeautifulSoup(page.content, 'html.parser')
    sites = []
    base_url = "http://catalog.illinois.edu"
    table = soup.findAll("div", {"class": "tab_content"})

    for rows in table:
        items = rows.findAll("li")
        for item in items:
            tup = ()
            tup = tup + (item.find('a').text,)
            tup = tup + (base_url + item.a.get("href"),)
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
    div = soup.find(id="minortextcontainer")
    if div is None:
        tables = soup.findAll("table", class_="sc_courselist")
    else:
        tables = div.findAll("table", class_="sc_courselist")
    # isRequired(tables)
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
            if len(req) > 0:
                courses.append(req)
    return courses

def fixCourses(courses):
    for core in courses:
        if (core == courses[0] and len(core) == 4):
            core = core + (1,)
        elif (len(core) < 4):
            if "foundation" in core[0]:
                core = core + (1,)
            else:
                core = core + (0,)

print(get_course_requirements(
    ("aging", "http://catalog.illinois.edu/undergraduate/aces/departments/ag-cons-econ/minor-environmental-economics-law/")))


# list = []
# sites = get_minor_sites()
# for i, site in enumerate(sites):
#     req = get_course_requirements(site)
#     if req is not None:
#         list.append(req)
# print(list)
