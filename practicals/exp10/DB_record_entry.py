import mysql.connector as mariadb

database_connection = mariadb.connect(
    user = 'varun',
    password = 'varun123',
    db = 'thakur'
)
cursor = database_connection.cursor()
try:
    query = "insert into student values(1001,'varun', 19, 99);"
    cursor.execute(query)
    database_connection.commit()
    print("record added sucessfully.")
except Error:
    print("something went wrong.")