#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).filter_by(name=argv[4]):
        print(data.id)
        exit()
    print("Not found")
    session.close()
