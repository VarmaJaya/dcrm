import mysql.connector # type: ignore

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Indra@123',
    )

#prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE elderco")

print("ALL done")
