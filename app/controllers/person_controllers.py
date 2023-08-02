
from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import person_model


@APP.route("/")
def index():
    return render_template("login_reg.html")


@APP.route("/register", methods=["POST"])
def register_user():
    if not person_model.Person.create_user(request.form):
        return redirect("/")
    return redirect("/dashboard")


@APP.route("/login", methods=["POST"])
def login_user():
    if person_model.Person.valid_login_data(request.form):
        return redirect("/dashboard")
    return redirect("/")





@APP.route("/logout")
def logout():
    session.clear()
    return redirect("/")







print("inside user controllers")
