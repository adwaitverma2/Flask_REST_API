from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = "secret123"  # Required for CSRF protection

# Define a form class
class NameForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello {form.username.data}, form validated successfully!"
    return render_template('form_wtf.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
