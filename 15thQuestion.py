# How do you capture URL parameters in Flask?
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    return f"Hello, {username}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"
