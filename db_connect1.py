import mysql.connector
# Using mysql-connector-python 
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
    #employee_delete_query = 'Delete from employee where id=4'

    # Here creating database table as employee
    #db_cursor.execute(employee_insert_query)
    #db_cursor.execute(employee_update_query)
    #db_cursor.execute(employee_delete_query)

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