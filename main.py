import requests
from bs4 import BeautifulSoup


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
    print(courses)
   


url = "http://catalog.illinois.edu/undergraduate/las/academic-units/math/mathematics-minor/"
get_course_requirements(url)
