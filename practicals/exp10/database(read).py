import mysql.connector as mariadb

database_connection = mariadb.connect(
    user = 'varun',
    password = 'varun123',
    db = 'thakur'
)
cursor = database_connection.cursor()

try:
    sql = "select * from employee"
    cursor.execute(sql)
    while True:
        record = cursor.fetchone()
        if record == None:
            break
        print(record)
    
    database_connection.close()
except Error:
    print("something went wrong.")