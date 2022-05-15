import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anisha@15",
  database="movies"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS movie (name VARCHAR(100) not null , actor VARCHAR(100) not null,actress VARCHAR(100) not null,director VARCHAR(100) not null,year_of_release YEAR not null)")
print("Table Created sucessfully")
print("**************************")

inp=int(input("Enter 1 to insert values to the table\nEnter 2 to display the values of the table\nEnter 3 to search a movie by actor name\n"))

if inp==1:
  print("Now insert values to the table")

  name = input("Enter the name of the movie: ")
  actor = input("Enter name of actor: ")
  actress = input("Enter the name of the actress: ")
  director = input("Enter the name of the director: ")
  year_of_release = input("Enter the year of release: ")

  sql = "INSERT INTO movie(name,actor, actress,director,year_of_release) values(%s, %s, %s,%s,%s)"
  val = (name,actor, actress,director,year_of_release)
  try:
      mycursor.execute(sql, val)

      mydb.commit()
  except:
      mydb.rollback()
  print(mycursor.rowcount, "Record inserted!")
  print("**************************")

elif inp==2:
  print("Displaying values of the table")
  mycursor.execute("SELECT * FROM movie")
  myresult = mycursor.fetchall()

  for row in myresult:
    print("Name = ", row[0], )
    print("Actor = ", row[1])
    print("Actress = ", row[2])
    print("Director = ", row[3])
    print("Year of release = ", row[4], "\n")
  print("**************************")

elif inp==3:
  act = input("Enter the name of the actor whose movie you wanna search: ")
  sql_select_query = "select * from movie where actor = %s"
  mycursor.execute(sql_select_query, (act,))
  record = mycursor.fetchall()
  for row in record:
      print("Movie= ", row[0], "\n")
  print("**************************")
else:
  print("Inavlid!!")

mydb.close()




