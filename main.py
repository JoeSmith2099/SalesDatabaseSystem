# Bradley Lloyd, Mehedi Nabil, Joseph Smith
# November 5, 2020
# This program takes in a preloaded sqlite3 database and allows the user to select whether they want to update it or change it
# around.

 #1. insert into all tables from Appendix D
 #2. display it all
 #3. Add five using Appendix E and display
 #4. Do the update
 #5. Do the delete
 #6. Do a search




import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None

    try:
      conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn   


# for inserting new values
def create_customer(conn, customer):
