from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import person_model, message_model, group_model
from flask import jsonify

@APP.route("/dashboard")
def user_dash():
    if 'user_id' not in session:
        return redirect("/")
    print("SESSION DASH ===>", session)
    return render_template("dashboard.html", 
                        all_users = person_model.Person.get_all_users(), 
                        chat_list = message_model.Message.logged_in_user_active_chats(session['user_id']),
                        group_chat_list = group_model.Group.view_all_group_chat_per_user(session['user_id'])    
                        )

@APP.route("/create-message", methods = ['POST'])
def new_msg():
    if 'user_id' not in session:
        return redirect("/")
    
    print("message request.form", request.form)
    if not message_model.Message.valid_message(request.form):
        return redirect('/dashboard')
    message_dict = {
        'content' : request.form['content'],
        'receiver_person_id' : request.form['receiver_person_id'],
        'sender_user_id' : session['user_id']
    }
    msg_receiver_id = message_dict['receiver_person_id']
    message_model.Message.create_message(message_dict)
    return redirect(f'/dm/{msg_receiver_id}')



@APP.route("/dm/<int:person_id>")
def direct_message(person_id):
    if 'user_id' not in session:
        return redirect("/")
    context_two = {
    'message_url': f'/dm/{person_id}'
}
    return render_template('dashboard.html',
                        all_users = person_model.Person.get_all_users(), 
                        chat_list = message_model.Message.logged_in_user_active_chats(session['user_id']),
                        message_hist =message_model.Message.read_all_messages_by_receiver(session['user_id'], person_id), context_two = context_two,
                        person_id = person_id )

@APP.route("/dm/update/<int:message_id>", methods=['POST'])
def updateMessage(message_id):
    if 'user_id' not in session:
        return redirect("/")
    print("REQUEST.json", request.json)
    message_model.Message.update_message(request.json)
    receiver_id = request.json['receiver_person_id']
    print("receiver id update **", receiver_id)
    # todo fix redirect. updates but doesn't redirect 
    return redirect(f'/dm/{receiver_id}')


@APP.route("/dm/delete/<int:message_id>", methods=['POST'])
def deleteMessage(message_id):
    if 'user_id' not in session:
        return redirect("/")
    deleted_message = message_model.Message.delete_message(message_id)
    # added this so I don't get an error
    if deleted_message == None:
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Failed to delete message"}), 400
