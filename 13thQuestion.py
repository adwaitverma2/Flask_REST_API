from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page!"

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"Search results for: {query}"

@app.route('/go')
def go():
    # Redirect to /search with ?q=flask
    return redirect(url_for('search', q='flask'))

@app.route('/profile')
def profile():
    user = request.args.get('user')
    age = request.args.get('age')
    return f"User: {user}, Age: {age}"

@app.route('/go_profile')
def go_profile():
    return redirect(url_for('profile', user='Adwait', age=25))

if __name__ == '__main__':
    app.run(debug=True)
