import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="powerrow",
  passwd="powerrow123!"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE minor_finder")

cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

for site in get_sites():
    vals = get_course_requirements(site)
    cursor.executemany(sql, vals)