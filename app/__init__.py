# Import the Flask application
from flask import Flask
# Import the Config class from config.py
from config import Config
# Import Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Import Flask-Migrate
from flask_migrate import Migrate


# Create instance of Flask class with the name "app"
app = Flask(__name__)

# Use Config class to import the SECRET_KEY from config.py
app.config.from_object(Config)

#Create an instance of SQLAlchemy to connect our app to the database
db = SQLAlchemy(app)

# Create an instance of Migrate that will track db and app
migrate = Migrate(app, db)



# import all of the routes from the routes.py and models from the models.py file into the current package
# (from the current directory, import routes.py)
from . import routes, models














# If youre running the script, then run the application
# if __name__ == '__main__':
#     app.run()
    # app.run(debug=True)


