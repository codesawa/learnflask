from app.auth import auth_bp
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.mail import send_mail
from threading import Thread
from app.models import User
from app import db


@auth_bp.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "GET":

        return render_template("login.html")
    
    email = request.form.get("email")

    password = request.form.get("password")

    remember_me = bool(request.form.get("remember"))

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):

        login_user(user, remember=remember_me)

        flash(f"welcome {user.name}", "success")

        return redirect(url_for("main.profile"))

    flash("Wrong email or password", "danger")

    return render_template("login.html")


@auth_bp.route("/signup" , methods=["POST", "GET"])
def signup():

    if request.method == "GET":

        return render_template("signup.html")
    
    email = request.form.get("email")

    name = request.form.get("name")

    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:

        redirect(url_for("auth.login"))

    new_user = User(
        email=email, name=name,
        password = generate_password_hash(password = password, salt_length=8)
    )
    db.session.add(new_user)

    db.session.commit()

    # email confirmation

    current_app.email_queue.enqueue(
        send_mail, 
        args=(
            current_app.config.get("MAIL_SENDER"),
            new_user.email, 
            f"Welcome to code sawa {name}"
        ), 
        job_ttl="1h"
    )

    return redirect(url_for("auth.login"))


@auth_bp.route("/logout")
def logout():

    logout_user()

    return "good bye"