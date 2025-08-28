from flask import Flask, url_for, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Generate URL for the 'about' route
    about_url = url_for('about')
    return f'<a href="{about_url}">Go to About Page</a>'

@app.route('/about')
def about():
    return "This is the About page!"

if __name__ == '__main__':
    app.run(debug=True)
