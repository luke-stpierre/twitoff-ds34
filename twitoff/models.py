from flask_sqlalchemy import SQLAlchemy


# Create DB Object
DB = SQLAlchemy()

# Create tables with schemas
# using a python class


class User(DB.Model):
    # ID and Username Columns
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    username = DB.Column(DB.String, nullable=False)
    # Newest tweet column
    newest_tweet_id = DB.Column(DB.BigInteger)
    
    
class Tweet(DB.Model):
    # ID, Text, and User ID Columns
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    text = DB.Column(DB.Unicode(300), nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    # Set up relationship between tables
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)
    # Word Embeddings Vector Storage Column
    vect = DB.Column(DB.PickleType, nullable=False)