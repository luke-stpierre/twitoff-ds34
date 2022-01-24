from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():

    app = Flask(__name__)
    # Configuration variables
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Connect database to app object
    DB.init_app(app)

    @app.route('/')
    def home():
        # query for all users in the database
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    @app.route('/populate')
    # Insert fake data into DB
    def populate():
        # Reset the database
        DB.drop_all()
        # Recreate the tables
        DB.create_all()
        
        # Make two users
        luke = User(id=1, username='lukestpierre')
        brian = User(id=2, username='brianmiller')
        
        # Make six tweets
        tweets = [Tweet(id=1, text='this is a luke tweet1', user=luke),
                  Tweet(id=2, text='this is a luke tweet3', user=luke),
                  Tweet(id=3, text='this is a luke tweet4', user=luke),
                  Tweet(id=4, text='this is a brian tweet5', user=brian),
                  Tweet(id=5, text='this is a brian tweet7', user=brian),
                  Tweet(id=6, text='this is a brian tweet8', user=brian)]
        
        # Insert them into the SQLite DB
        DB.session.add(luke)
        DB.session.add(brian)
        for tweet in tweets:
            DB.session.add(tweet)
        
        # Commit the DB changes
        DB.session.commit()
        
        return render_template('base.html', title='Populate')
    
    @app.route('/reset')
    def reset():
        # Drop all DB tables
        DB.drop_all()
        # Recreate User and Tweet tables
        DB.create_all()
        
        return render_template('base.html', title='Reset Database')
    
    return app