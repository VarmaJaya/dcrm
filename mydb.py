import mysql.connector # type: ignore

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'Your user name',
    passwd = 'your password',
    )

#prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE elderco")

print("ALL done")
