import mysql.connector

#connecting first without specifying the db
dataBase = mysql.connector.connect(
    host="localhost",
    user="jimmy",
    password="Jimmy@123",
    )

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a new database
cursorObject.execute("CREATE DATABASE crm")


dataBase.close()


#Now reconnecting to the database created 'crm'

dataBase = mysql.connector.connect(
    host="localhost",
    user="jimmy",
    password="Jimmy@123",
    database="crm"
    )

cursorObject = dataBase.cursor()


