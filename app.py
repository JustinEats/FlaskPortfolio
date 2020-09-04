from flask import flask, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MPFIGBRGWISF24'
debug = DebugToolbarExtension(app)

app.route('/')
def home_page():
    return render_template('home-page.html')

app.route('/about-me')
def about_me_page():
    return render_template('about-me.html')