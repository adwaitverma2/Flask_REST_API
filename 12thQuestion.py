from flask import Flask, render_template

app = Flask(__name__)

# Define custom filter
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/')
def index():
    return render_template("index2.html", name="Adwait")

if __name__ == '__main__':
    app.run(debug=True)
