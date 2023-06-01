
from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import person_model
from app.models import recipe_model


@APP.route("/")
def index():
    return render_template("login_reg.html")


@APP.route("/users/register", methods=["POST"])
def register_user():
    if not person_model.Person.create_user(request.form):
        return redirect("/")
    return redirect("/users/dashboard")


@APP.route("/users/login", methods=["POST"])
def login_user():
    if person_model.Person.valid_login_data(request.form):
        return redirect("/users/dashboard")
    
    return redirect("/")


@APP.route("/users/dashboard")
def user_dash():
    if 'user_id' not in session:
        return redirect("/")
    print("SESSION DASH ===>", session)
    recipes_by_user = recipe_model.Recipe.get_all_recipes_by_user()
    return render_template("dashboard.html", recipes_by_user=recipes_by_user)


@APP.route("/users/logout")
def logout():
    session.clear()
    return redirect("/")







print("inside user controllers")
