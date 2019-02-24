import mysql.connector
import requiredcourses

db = mysql.connector.connect(
  host="localhost",
  user="MySQL80",
  passwd="powerrow"
)

# cursor.execute("CREATE TABLE dars (COURSENAME VARCHAR (255) NOT NULL, GRADE VARCHAR (255) NOT NULL, CREDITHOURS INT NOT NULL, TERM VARCHAR (255))")
# values = [
#     ('MATH 125', 'IP', 3, 'SP 19'),
#     ('STAT 200', 'PS', 3, 'SP 18'),
#     ('STAT 400', 'A', 3, 'FA 18')
# ]
# cursor.executemany(query, values)

# cursor.execute("CREATE TABLE minor (COURSENAME VARCHAR (255) NOT NULL, REQUIRED INT NOT NULL, TYPE INT, SUBCATEGORY VARCHAR(255), NUMSUBCATEGORIES INT, CLASSESPERCAT INT, HOURSPERTYPE INT, CREDITHOURS INT, TOTALHOURS INT)")
# query2 = "INSERT INTO minor VALUES (%s, %d, %d, %s, %d, %d, %d, %d, %d)"
# values2 = [
#     ('MATH 125', 0, 2, NULL, NULL, NULL, 2, 3, 18),
#     ('MATH 225', 0, 2, NULL, NULL, NULL, 2, 2, NULL),
#     ('MATH 415', 0, 2, NULL, NULL, NULL, 2, 3, NULL),
#     ('ACE 261', 0, 3, NULL, NULL, NULL, 3, 4, NULL),
#     ('CPSC 241', 0, 3, NULL, NULL, NULL, 3, 3, NULL),
#     ('STAT 100', 0, 3, NULL, NULL, NULL, 3, 3, NULL),
#     ('STAT 200', 0, 4, NULL, NULL, NULL, 3, 3, NULL),
#     ('STAT 212', 0, 4, NULL, NULL, NULL, 3, 3, NULL),
#     ('STAT 400', 1, NULL, NULL, NULL, NULL, NULL, 4, NULL),
#     ('STAT 420', 1, NULL, NULL, NULL, NULL, NULL, 3, NULL)
# ]
# cursor.executemany(query2, values2)
# db.commit()

def getCoursesLeft(minor, dars):
  cursor = db.cursor()
  courses_left = []

  #get hours required per minor
  cursor.execute("SELECT minor.TOTALHOURS FROM minor LIMIT 1")
  hours_left = cursor.fetchall()

  #~~execute just returns number of rows changed/retrieved~~

  #subtract credit hours left based on fulfilled required courses
  cursor.execute("SELECT SUM(minor.CREDITHOURS) FROM dars INNER JOIN minor WHERE minor.REQUIRED = 1 AND dars.COURSENAME = minor.COURSENAME")
  hourse_left -= cursor.fetchall()

  #get REQUIRED classes left
  cursor.execute("select minor.COURSENAME from minor left join dars on dars.COURSENAME=minor.COURSENAME where dars.COURSENAME is NULL AND minor.REQUIRED=1")
  required_classes_left = cursor.fetchall()
  for curr in required_classes_left:
    #get list of required courses HOURS
    cursor.execute("select minor.CREDITHOURS from minor left join dars on dars.COURSENAME=minor.COURSENAME where dars.COURSENAME is NULL AND minor.REQUIRED=1")
    hours = cursor.fetchall()
    for hour in hours:
      req = RequiredCourses(1, hour, curr)
      courses_left.append(req)

  #get list of diff types
  cursor.execute("SELECT minor.TYPE FROM minor WHERE minor.REQUIRED=0")
  types = cursor.fetchall()

  #loop through types and do things accordingly
  for type in types:
    #get required hours per type
    cursor.execute("SELECT minor.HOURSPERTYPE FROM minor WHERE TYPE=2 LIMIT 1")
    requiredhours = cursor.fetchall()

    #get classes fulfilled
    cursor.execute("SELECT minor.COURSENAME FROM minor, dars WHERE minor.REQUIRED=0 AND TYPE=%d AND minor.COURSENAME=dars.COURSENAME" % type)
    fulfilled = cursor.fetchall()
    if len(fulfilled) is 0:
        #get list of courses that are options 
        cursor.execute("SELECT minor.COURSENAME FROM minor WHERE minor.REQUIRED=0 AND TYPE=%d" % type)
        coursespertype = cursor.fetchall()
        cursor.execute("SELECT minor.HOURSPERTYPE FROM minor WHERE minor.REQUIRED=0 AND TYPE=%d LIMIT 1" % type)
        hours_per_type = cursor.fetchall()
        arr = []
        for course in coursespertype:
            arr.append(RequiredCourses(1, hours_per_type, course)) #need to change, not always 1
        courses_left.append(arr)
        
    else: 
        #subtract hours from required hours since this type has been fulfilled
        #need to change bc subcategories
        cursor.execute("SELECT minor.CREDITHOURS FROM minor, dars WHERE TYPE=%d AND minor.COURSENAME=dars.COURSENAME LIMIT 1" % type)
        hours_left -= cursor.fetchall()

    return (courses_left, hours_left)


  



#sql = "INSERT INTO dars (term, classname, credits, grade) VALUES (%s, %s, %d, %s)"

#vals = get_completed_courses(filename) #suhi and irdina
#cursor.executemany(sql, vals)
