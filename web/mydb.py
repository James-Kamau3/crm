import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="crm"
    )

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a new database
cursorObject.execute("CREATE DATABASE crm")

print("Database created")

