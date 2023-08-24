from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import person_model, message_model, group_model


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
    
    
    print("new group data ----> ", new_group)
    # request.form.getlist pulls all the ids from the form
    # request.form.getlist is a LIST!!
    selected_users = request.form.getlist('group_members')
    
    for user_id in selected_users:
        new_group_member = group_model.GroupMembers.create_members_per_group(new_group, user_id)
        print(f"Group member {user_id} was added to the DB! Here is the new group member info {new_group_member}")
    
    add_creator_to_chat = group_model.GroupMembers.create_members_per_group(new_group, session['user_id'])
    return redirect('/dashboard')
    # return "Success"

@APP.route('/group-chat/<int:group_id>')
def view_group_chat(group_id):
    pass








# @APP.route("/")


# @APP.route("/")


# @APP.route("/")