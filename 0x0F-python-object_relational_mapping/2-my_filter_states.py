#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                   ORDER BY id".format(argv[4]))
        table = db.fetchall()
        for data in table:
            print(data)
