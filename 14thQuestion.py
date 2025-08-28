from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {"name": "Adwait", "age": 25, "role": "Developer"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
