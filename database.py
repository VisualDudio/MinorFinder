import mysql.connector
import DARS_parser
import matching

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="powerrow"
)

cursor = db.cursor()
cursor.execute("USE mydatabaselol")
# (COURSENAME VARCHAR (255) NOT NULL, GRADE VARCHAR (255) NOT NULL, CREDITHOURS INT NOT NULL, TERM VARCHAR (255)
#cursor.execute("CREATE TABLE dars (COURSENAME VARCHAR (255) NOT NULL, TERM VARCHAR (255), CREDITHOURS INT NOT NULL, GRADE VARCHAR (255) NOT NULL)")

#cursor.execute("CREATE TABLE minor (COURSENAME VARCHAR (255) NOT NULL, REQUIRED INT NOT NULL, TYPE INT, SUBCATEGORY VARCHAR(255), NUMSUBCATEGORIES INT, CLASSESPERCAT INT, HOURSPERTYPE INT, CREDITHOURS INT, TOTALHOURS INT)")

courses = DARS_parser.get_courses()
matching.get_top_minors(courses)

# for site in get_sites():
#     vals = get_course_requirements(site)
#     cursor.executemany(sql, vals)



cursor.execute("SHOW TABLES")
for (table_name,) in cursor:
  print(table_name)