# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "employee"
)
# create a query
empid = int(input("Enter employee id : "))
name = input("Enter name : ")
Department = (input("Enter Department : "))
email = input("Enter Email id :")
salary = int  (input("Enter salary : "))
date_of_joining= input("Enter date of joining(YYYY-MM-DD):")


query = f"insert into employees values ({empid}, '{name}', '{Department}', '{email}', {salary},'{date_of_joining}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()