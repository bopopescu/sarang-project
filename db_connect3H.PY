import mysql.connector

try:

    # Creating connection object-
    con = mysql.connector.connect(
        host= "localhost",
        user= "root",
        passwd= "",
        database= "my_second_db"
    
    )

    print(con)
    # Create curser as pointer for perform database operation
    db_cursor = con.cursor()

    # Create database
    #db_cursor.execute("CREATE DATABASE my_third_db")

    # To create table
    #db_cursor.execute("CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT(10))")

    #Creating insert query
    product_insert_query = 'INSERT INTO product (name, price) values ("spickers_3", 200)'

    # Here creating database table as employee
    db_cursor.execute(product_insert_query)

    con.commit()  # commit() to save data in database after update delete query

    #Getting all rows from your table to display
    db_cursor.execute("SELECT * from product")

    

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

