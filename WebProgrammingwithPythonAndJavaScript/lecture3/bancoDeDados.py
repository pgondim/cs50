import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import csv

engine = create_engine(os.getenv("postgres://ealkcgshhniymr:4ac2985e6d14b05aa78f13369ecf13ec0489edd1119a9d3f57ee6400560ce2c7@ec2-34-197-212-240.compute-1.amazonaws.com:5432/d1pa4mslfvd7o9"))       # database engine object from SQLAlchemy that manages connections to the database
"""                                                        # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))          # create a 'scoped session' that ensures different users' interactions with the
                                                        # database are kept separate

f = open("flights.csv")
reader = csv.reader(f)
for origin, destination, duration in reader: # loop gives each column a name
    db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
              {"origin": origin, "destination": destination, "duration": duration}) # substitute values from CSV line into SQL command, as per this dict
    print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")

db.commit() # transactions are assumed, so close the transaction finished
"""