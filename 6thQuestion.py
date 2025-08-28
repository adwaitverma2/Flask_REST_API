from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form['username']  # Extract form data
    return f"Hello, {username}! Form submitted successfully."

if __name__ == '__main__':
    app.run(debug=True)
