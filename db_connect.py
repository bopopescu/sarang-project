import mysql.connector
from mysql.connector import Error, errorcode
# USing mysql-connector

'''
# Creating connection object-
con = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "",
    database= "my_first_db"
    #port= 3307 if different port is working as 3306 is default port
)
print(con)
# Create curser as pointer for perform database operation
db_cursor = con.cursor()

# to create table
#db_cursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

#alter table
#db_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")
#db_cursor.execute("ALTER TABLE student ADD class VARCHAR(5) NOT NULL AFTER name")
#insert_query = "INSERT INTO employee(name, salary) VALUES('Jim', '27000')" #no need to specify ID as its auto update primary key
#insert_query = "INSERT INTO student(id, name, class) VALUES(1,'Jon', '10th')"

db_cursor.execute(insert_query)

con.commit()  # commit() to save data in database after update delete query

db_cursor.execute("SELECT * from student") #fetch all data in db curser

#result = db_cursor.fetchone()
#result = db_cursor.fetchmany(size=2)

result = db_cursor.fetchall() #save all data in result using fetchall method in db_curser

for row in result:
    print(row)

# get list of all databases
db_cursor.execute("SHOW TABLES")

# print all databases
for table in db_cursor:
    print(table)
'''


try:

    # Creating connection object-
    con = mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "",
        database= "my_first_db"


    )
    #Checking/Printing connection object
    print(con)
    
    # Create curser as pointer for perform database operation
    db_cursor = con.cursor()

    print(db_cursor)

    #Creating insert query
    #employee_insert_query = 'INSERT INTO employee (name, salary) values ("Alok", 20000)'
    #employee_update_query = 'Update employee set name = "Steve", salary = 35000 where id= 3'
    employee_delete_query = 'Delete from employee where id=4'

    # Here creating database table as employee
    #db_cursor.execute(employee_insert_query)
    #db_cursor.execute(employee_update_query)
    db_cursor.execute(employee_delete_query)

    #commiting-
    con.commit()

    #Getting all rows from your table to display
    db_cursor.execute("SELECT * from employee")

    result = db_cursor.fetchall() #Fetchall method called to get

    for row in result:
        print(row)

    db_cursor.close()

except mysql.connector.Error as Error:
    print(f"Data Insertion Failed due to {Error}")

finally:
    if(con.is_connected()):
        con.close()
        print("Connection Object Closed Successfully.")


