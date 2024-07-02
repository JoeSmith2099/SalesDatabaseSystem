# Bradley "Astro-Man" Lloyd, Mehedi "Hedi of the State" Nabil, Joseph "Wiffle BatBoy" Smith
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
  """
  Create a new customer into the customer table
  :param conn:
  :param customer:
  :return: customer id
  """
  print("Customer Data Created Successfully. The Created Records are: ")
  sql = ''' INSERT OR REPLACE INTO customer (customer_number,customer_type,customer_name,customer_contact_email)  
          VALUES (?,?,?,?);'''
  cur = conn.cursor()
  cur.execute(sql, customer)
  conn.commit()

  return cur.lastrowid

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

    conn.close()



def main():
  database = "SalesDatabase.db"
  print("Welcome to Sales Order Management System. ")

  conn = create_connection(database) 
  with conn:
    customer = (100, 'Robert', 'Downey', 'RDowney@gmail.com')
    customer_id = create_customer (conn, customer)
    task_1 =(200, 'Scarlett', 'Johansson', 'SJohansson@yahoo.com')
    task_2 = (100, 'Robert', 'Downey', 'RDowney@gmail.com')
    task_3 = ()
    print(task_1)
    create_customer(conn, task_1)
    create_customer(conn,task_2)

if __name__ == '__main__':
    main()
    