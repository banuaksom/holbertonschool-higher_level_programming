#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    ORDER by cities.id")
        table = db.fetchall()
        for data in table:
            print(data)
