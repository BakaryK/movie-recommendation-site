from flask import Blueprint

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return "<h1>This will be the home page</h1?"

@views.route('/recommendations')
def recommend():
    return "<h1>This will display movie recommendations</h1>"

@views.route('/watchlist')
def watchlist():
    return "<h1>This will display previously watched movies</h1?"

