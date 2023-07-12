import sqlite3

connection = sqlite3.connect('./database/kratom.db')
cursor = connection.cursor()

cursor.execute("select * from users")
for row in cursor.fetchall():
    print(row)
    
connection.close()