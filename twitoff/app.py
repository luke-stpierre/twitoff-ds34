from flask import Flask, render_template
from .models import DB, User, Tweet
from os import getenv
from .twitter import add_or_update_user

def create_app():

    app = Flask(__name__)
    # Configuration variables
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Connect database to app object
    DB.init_app(app)

    @app.route('/')
    def home():
        # query for all users in the database
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    @app.route('/populate')
    # Populate the DB with real Tweets
    def populate():
        # Adding some users
        add_or_update_user('nasa')
        add_or_update_user('joebiden')
        add_or_update_user('lukestpierre6')
        
        return render_template('base.html', title='Populate')
    
    @app.route('/update')
    def update():        
        usernames = get_usernames()
        for username in usernames:
            add_or_update_user(username)
            
        return render_template('base.html', title='Update Tweets')
    
    
    @app.route('/reset')
    def reset():
        # Drop all DB tables
        DB.drop_all()
        # Recreate User and Tweet tables
        DB.create_all()
        
        return render_template('base.html', title='Reset Database')
    
    return app


def get_usernames():
    # get all of the usernames of existing users
    Users = User.query.all()
    usernames = []
    for user in Users:
        usernames.append(user.username)       
    return usernames