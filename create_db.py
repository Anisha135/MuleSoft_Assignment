import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anisha@15"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE movies")
print("Database created sucessfully")
mydb.close()