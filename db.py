'''
MySQL Database connection (XAMPP)
Before starting with the code, make sure you have installed pymysql $pip install pymysql
'''

import pymysql

hostname = 'Your-HostName'
username = 'Your-UserName'
password = 'Your-Password'
database = 'Your-DatabaseName'

# database connection
connection = pymysql.connect(hostname, username, password, database)
cursor = connection.cursor()

# querying the table demo
get_details = 'select * from demo'
cursor.execute(get_details)
rows = cursor.fetchall()

print(rows)

# Updating table demo
update_sql = "UPDATE  demo SET name = 'abc'  WHERE id = '3' ;"
cursor.execute(update_sql)

# mandatory step to reflect changes to database
connection.commit()

