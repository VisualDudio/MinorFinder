import requests
from bs4 import BeautifulSoup

def is_course_row(css_class):
    return css_class == "even" or css_class == "odd"

page = requests.get("http://catalog.illinois.edu/undergraduate/engineer/departments/comp-sci/#text")
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.findAll("table", class_="sc_courselist")

for table in tables:
    rows = table.findAll("tr", class_=is_course_row)
    print(rows)
    break