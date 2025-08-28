from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "my_secret_key"  # Required for signing session cookies

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome back, {session['username']}!"
    return "You are not logged in. <a href='/login'>Login here</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']  # Store in session
        return redirect(url_for('home'))
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Enter username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
