#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. Safe from MySQL injections!
"""
import MySQLdb
from sys import argv

with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                     db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
        table = db.fetchall()
        for data in table:
            print(data)
