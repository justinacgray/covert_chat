from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import person_model, message_model


@APP.route("/dashboard")
def user_dash():
    if 'user_id' not in session:
        return redirect("/")
    print("SESSION DASH ===>", session)
    return render_template("dashboard.html", all_users = person_model.Person.get_all_users())



@APP.route("/create-message", methods = ['POST'])
def new_msg():
    print("message request.form", request.form)
    if not message_model.Message.valid_message(request.form):
        return redirect('/dashboard')
    message_dict = {
        'content' : request.form['content'],
        'receiver_user_id' : request.form['receiver_person_id'],
        'sender_user_id' : session['user_id']
    }
    
    message_model.Message.create_message(message_dict)
    
    return redirect('/dashboard')



# @APP.route("/")


# @APP.route("/")


# @APP.route("/")

