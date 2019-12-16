#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT cities.name FROM cities\
                    LEFT JOIN states\
                    ON cities.state_id=states.id\
                    WHERE states.name = %s\
                    ORDER by cities.id", (argv[4],))
        table = db.fetchall()
        print(", ".join([data[0] for data in table]))
