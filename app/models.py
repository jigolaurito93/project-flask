# Import the instance of SQLAlchemy
from app import db
from datetime import datetime

# Module that generates a password hash and checks the password 
from werkzeug.security import generate_password_hash, check_password_hash

# Define a class called User and it will inherit from the db.model
class User(db.Model):
    # Specify the columns
    id = db.Column(db.Integer, primary_key=True)
    # In reference to signup form
    # VarChar(50)
    # Nullable when set to False, will cause the "NOT NULL" phrase to be added when generating DDL for the column
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # unique = True is used so that only one user can have that email address
    email = db.Column(db.String(75), nullable=False, unique=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    # default time will be the current time
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # It's gonna be looking in it in the keyword arguments for the password key and whatever the value is associated with that key, were gonna hash that and save it as the password attribute
        self.password = generate_password_hash(kwargs.get('password'))
        # db session connects to the database, "add" adds the user to the database
        # self is the model object that we just created
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        # This prints when the object is called on flask shell
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess): 
        # check_password_hash return a True or False statement
        # It takes the password hash for the first argument and password_guess is whatever was input in login
        # It compares the 2 passwords if its True or False
        return check_password_hash(self.password, password_guess)
