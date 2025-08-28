from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Define a simple route
@app.route("/")
def home():
    return "Hello, Flask! This is my first app." 

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
