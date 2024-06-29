"""
# Sales Order Management System

## Authors
- Bradley "Astro-Man" Lloyd
- Mehedi "Hedi of the State" Nabil
- Joseph "Wiffle BatBoy" Smith

## Date
- November 5, 2020

## Description
This Python program provides functionality to manage a sales order database using SQLite. 
The program allows users to perform various operations on the database, including:
1. Inserting data into all tables (Appendix D).
2. Displaying all records.
3. Adding five new records (Appendix E) and displaying them.
4. Updating existing records.
5. Deleting specific records.
6. Searching for specific records.
7. Deleting all records and closing the database.

## Usage
The script connects to a preloaded SQLite database and provides functions to update and modify the data within it. 
Follow the instructions in the `main()` function to see the usage examples.

## Requirements
- Python 3.x
- SQLite3

## Instructions
1. Ensure you have Python 3.x and SQLite3 installed.
2. Place the database file (`Milestone2-Group-Team_A.db`) in the same directory as the script.
3. Run the script using a Python interpreter.

## Functions (Tentative)
- `create_connection(db_file)`: Establish a connection to the SQLite database.
- `create_customer(conn, customer)`: Insert or replace a customer record.
- `select_all_customers(conn)`: Query and display all customer records.
- `update_customer(conn, customer)`: Update a customer's information.
- `delete_customer(conn, customer_number)`: Delete a customer by their number.
- `search_customer(conn, customer_number)`: Search for a customer by their number.
- `delete_all_customers(conn)`: Delete all customer records.

## Contact
For any questions or issues, please contact the authors via their GitHub profiles.
"""
