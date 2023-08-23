from app import APP
from flask import render_template, redirect, request, session, flash
from app import socketio
from flask_socketio import SocketIO, emit
from app.models import person_model, message_model, group_model
# socketio = SocketIO()

users = {}

@APP.route("/group-chat")
def render_group_chat(): 
    if 'user_id' not in session:
        return redirect("/")
    return render_template("dashboard.html", all_users = person_model.Person.get_all_users(), chat_list = message_model.Message.logged_in_user_active_chats(session['user_id']))

@APP.route('/create-group-chat', methods= ['POST'])
def create_group_and_members():
    new_group_dict = {
        "group_name" : request.form['group_name'],
        "creator_user_id" : session['user_id'],
        "group_members" : request.form.getlist("group_members")
    }
    
    print("##### GROUP MEMBERS ######", new_group_dict)
    
    new_group = group_model.Group.create_group(new_group_dict)
    
    new_group_member = group_model.GroupMembers.create_members_per_group()
    # todo - need to get a list of users from request.form
    
    return redirect('/dashboard')


@socketio.on('connect')
def enter_group():
    print('shalom friend')
    

@socketio.on('user_join')
def user_enters(username):
    print(f" Shalom {username}! ")
    users[username] = request.sid




# @APP.route("/")


# @APP.route("/")


# @APP.route("/")