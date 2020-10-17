import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="your_username_here",
  passwd="your_mysql_password_here",
  database="your_database_name_here"
)
if mydb.cursor:
    print("done")
