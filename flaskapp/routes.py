from flaskapp import app, db
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return redirect(url_for('register'))
        return render_template("home.html", title="Instaclone")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = 
