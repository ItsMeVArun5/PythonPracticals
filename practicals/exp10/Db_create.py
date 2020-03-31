import mysql.connector as mariadb

database_connection = mariadb.connect(
    user = 'varun',
    password = 'varun123',
    db = 'thakur'
)
cursor = database_connection.cursor()

try:
    table = "create table student(id integer, name varchar(20), age integer, marks integer);"
    cursor.execute(table)
    print("table created successfully.")
except Error:
    print("something went wrong.")