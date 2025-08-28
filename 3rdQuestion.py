from flask import Flask, request

app = Flask(__name__)

# GET request route
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, this is a GET request!"

# POST request route
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get("name")  # Example: reading form data
    return f"Hello {data}, this is a POST request!"

# Same route with different methods
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return "You sent a GET request to /user"
    elif request.method == 'POST':
        return "You sent a POST request to /user"

if __name__ == '__main__':
    app.run(debug=True)
