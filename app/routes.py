# (from the app folder, import the instance of app inside the init.py file)
from app import app, db
# Import the render_template module from flask
from flask import render_template, redirect, url_for, flash
# import fake posts form fake data
from fake_data import posts
# import the signup form from forms.py
from app.forms import SignUpForm, LoginForm
from app.models import User

# Create a decorator
@app.route('/') #127.0.0.1:5000/
def index():
    # Renders the index.html file
    # Takes 2 arguments, the name of the template AND the variables you want to pass to the template engine as keyword argument arguments
    return render_template('index.html', posts=posts)

@app.route('/signup', methods=['GET', "POST"]) #127.0.0.1:5000/signup
def signup():
    # Create an instance of SignUpForm()
    # Import SignUpForm from app.forms
    form = SignUpForm()

    # If sign up is successful and all are fields are valid
    if form.validate_on_submit():
        # If successful, extract the data from the form fields
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check to see if there is already a user with either that username or email
        # Import db from app
        #Filter to check if the user.username is equal to username or User.email is equal to email and already in the database
        check_user = db.session.execute(db.select(User).filter((User.username == username) | (User.email == email))).scalars().all()
        # If true
        if check_user:
            # Flash a message saying that user with email/username already exists
            flash("A user with that username and/or email already exists", "warning")
            # Redirect to the same page (SignUp page)
            return redirect(url_for("signup"))
        # If check_user is empty, create a new record in the user table
        new_user = User(first_name= first_name, last_name=last_name, email=email, username=username, password=password)

        # Flashes an alert message
        # Accessed on the next request ('index')
        # Import flash in flask module
        flash(f"Thank you {new_user.username} for signing up", 'success')
        # If successful, redirect to the specified page
        # Call in the function (index)
        # Import url_for and redirect from flask
        return redirect(url_for('index'))
    
    # If sign up is unsuccessful
    else:
        print('did not valudate')
    # Pass that form as a variable named form
    return render_template('signup.html', form=form)

@app.route('/login', methods=["POST", "GET"]) #127.0.0.1:5000/login
def login():
    # Create an instance of login form
    # Import LoginForm from app.forms
    form = LoginForm()

    # If form is successfully submitted, extract the data from the fields
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username, password)
        # Check if there is a user with that username and password
        # If password and username are not matched, redirect to the same page, "login page"
        user = User.query.filter_by(username=username).first()
        # If the username exists, it will give back a user object
        # If username does not exist, we get back None
        # If the user is not None, meaning we get back a user AND we call back a check_password method with the password that we input from the form:
        # Flash a message indicating that the user has logged in successfully
        if user is not None and user.check_password(password):
            flash(f'You have successfully logged in as {username} !', 'success')
            # Redirect to index.html
            return redirect(url_for('index'))
        
        # If its false, flash a message indicating that its an invalid username
        # Redirects it to the same page (login)
        else:
            flash(f'Invalid username and/or password. Please try again.', 'danger')
            return redirect(url_for('login'))

        # If login is successful, redirect to the index page, flash a message

    return render_template('login.html', form=form)