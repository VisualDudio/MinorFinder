# import requests
from bs4 import BeautifulSoup
import urllib3
import csv
import re

def get_courses():
    courses_list = []
    all_courses = soup.findAll("tr", class_="takenCourse")

    for curr in all_courses:
        # create and populate a 'course' tuple and add it to courses
        term = curr.find("td", class_="term").get_text().strip()
        class_name = curr.find("td", class_="course").get_text().strip()
        class_name = format_course_name(class_name)
        credit = curr.find("td", class_="credit").get_text().strip()
        grade = curr.find("td", class_="grade").get_text().strip()
        
        course = (term, class_name, credit, grade)
        courses_list.append(course)              
    
    return courses_list

def format_course_name(course_name):
    split = course_name.split()
    split[:1]
    return split[0] + ' ' + split[1]

file = open("test.html")
soup = BeautifulSoup(file, features="html.parser")
print(get_courses())

# def process_course_info(info):
#     formatted = info.encode('ascii', errors = 'ignore').decode('utf-8') #remove non-ascii chars
#     formatted = re.sub(r'\s+', ' ', info)
#     return formatted


# all_courses = soup.findAll("table", class_="completedCourses")

# for course in all_courses:
#     print(course)






# def is_course_row(css_class):
#     return css_class == "even" or css_class == "odd"

# page = requests.get("http://catalog.illinois.edu/undergraduate/engineer/departments/comp-sci/#text")
# soup = BeautifulSoup(page.content, 'html.parser')

# tables = soup.findAll("table", class_="sc_courselist")

# for table in tables:
#     rows = table.findAll("tr", class_=is_course_row)
#     print(rows)
#     break

file.close()