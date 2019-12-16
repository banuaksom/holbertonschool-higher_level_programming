#!/usr/bin/python3
"""
Lists all states with a name starting with upper N from the database
hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                   ORDER BY id")
        table = db.fetchall()
        for data in table:
            print(data)
