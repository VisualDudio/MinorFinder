# import requests
from bs4 import BeautifulSoup
import requests
import urllib3
import csv
import re

def get_courses():
    courses_list = []
    #temp_list = []
    course_names = []
    all_courses = soup.findAll("tr", class_="takenCourse")

    for curr in all_courses:
        # create and populate a 'course' tuple and add it to courses
        term = curr.find("td", class_="term").get_text().strip()
        name = curr.find("td", class_="course").get_text().strip()
        class_name = format_course_name(name)
        credit = int(float((curr.find("td", class_="credit").get_text().strip())))
        grade = curr.find("td", class_="grade").get_text().strip()
        
        course = (term, class_name, credit, grade)
        
        if course not in courses_list and name not in course_names and credit > 0:
            course_names.append(class_name)
            courses_list.append(course)

    #print(courses_list) # for our viewing only 
    return courses_list

def format_course_name(course_name):
    split = course_name.split()
    split[:1]
    return split[0] + ' ' + split[1]


# page = requests.get("https://uachieve.apps.uillinois.edu/uachieve_uiuc/audit/read.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(get_courses())

file = open("test.html")
soup = BeautifulSoup(file, features="html.parser")
get_courses()
file.close()