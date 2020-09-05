from flask import Flask, render_template, redirect, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MPFIGBRGWISF24'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template('home-page.html')


@app.route('/contact')
def contact_page():
    return render_template('contact-page.html')


@app.route('/contact-post', methods=['POST'])
def contact():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['comment'] = request.form['comment']
    flash('Messege sent! Thank you! Justin will get back to you as soon as possible!')
    return redirect('contact-page.html')
