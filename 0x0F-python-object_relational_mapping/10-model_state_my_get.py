#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # engine Creation APIDB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Session for make a queries to db
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query to bd(argv[3]) for table State avoid SQL inyection
    if ";" not in sys.argv[4]:
        state = session.query(State).filter(
            State.name.like(sys.argv[4])).order_by(State.id)
        if (state.all()):
            for i in state.all():
                print(i.id)
        else:
            print("Not found")
    session.close()
