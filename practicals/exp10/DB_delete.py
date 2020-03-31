import mysql.connector as mariadb

database_connection = mariadb.connect(
    user = 'varun',
    password = 'varun123',
    db = 'thakur'
)
cursor = database_connection.cursor()

try:
    remove = "delete table student;"
    cursor.execute(remove)  
    print("sucessfully removed table in database")
except Error:
    print("something went wrong.")