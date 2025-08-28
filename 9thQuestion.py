from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the home page."

@app.route('/login')
def login():
    # Redirect user to dashboard after login
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
