# import module of mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "employee"
)

def update_employee(empid,salary):
    conn = get_connection()


    query = f"update employees SET salary=%s where empid=%s;"
    val=(salary,empid)

    # create a cursor to execute the query
    cursor = conn.cursor()

    # execute query using cursor
    cursor.execute(query,val)

    # after execution of query commit your changes
    conn.commit()

    # close the cursor
    cursor.close()

    #close the connection with mysql server 
    conn.close()

update_employee(101,70000)