"""Models and database functions for cars db.""" ### ??? I don't understand functions for cars ???###

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
#Part 1: Compose ORM

class Human(db.Model):
    """Human model."""

    __tablename__ = "humans"   #repr included ?
    
    human_id = db.Column(db.Integer,primary_key=True, nullable=False)# PK corresponds to public.humans table (psql)
    fname = db.Column(db.String(25), nullable=False)                 #\d humans
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    animals = db.relationship('Animal')                       #relationship using FK and __repr__

class Animal(db.Model):
    """Animal model."""

    __tablename__ = "animals"   #repr included ?
    animal_id = db.Column(db.Integer, primary_key=True, nullable=False)  #corresponds to public.animals (psql)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'), nullable=False)  #\d animals
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)# do i need to add the max integer ?

    humans = db.relationship('Human')
#End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    init_app()
