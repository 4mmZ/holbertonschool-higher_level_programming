#!/usr/bin/python3

import sys
import MySQLdb

def list_from_database(mysql_username, mysql_passwd, database_name, state_name_searched):
    db = MySQLdb.connect(
        host="localhost",
        user= mysql_username,
        passwd= mysql_passwd,
        db= database_name,
        port=3306)

    cursor = db.cursor()

    # Execute the query to fetch all states
    clean_state_name = db.escape_string(state_name_searched)
    query = "SELECT * FROM states WHERE name LIKE '{clean_state_name}%' ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

        # Display the results
    for state in states:
        print(state)

        # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == '__main__':
    from sys import argv

    username = argv[1]
    psswd = argv[2]
    database = argv[3]
    state_name= argv[4]

    list_from_database(username, psswd, database, state_name)
