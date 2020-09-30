from flask import Flask
from .db_model import DB

def create_app():
    '''Create and configure an instance our Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////twitoff.db'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    DB.init_app(app) # connects flask app to SQLalchemy DB

    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    return app