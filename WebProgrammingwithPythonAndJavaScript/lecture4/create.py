import os

from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres://ealkcgshhniymr:4ac2985e6d14b05aa78f13369ecf13ec0489edd1119a9d3f57ee6400560ce2c7@ec2-34-197-212-240.compute-1.amazonaws.com:5432/d1pa4mslfvd7o9")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being un yet).
db.init_app(app)

def main():

    # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()