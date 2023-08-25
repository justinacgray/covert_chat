
# importing socketio from APP since the instance was created in the init file
from app import APP, socketio
from flask import render_template, redirect, request, session, flash
from flask_socketio import emit


users = {}


@socketio.on('connect')
def enter_group():
    print('shalom friend')
    

@socketio.on('user_join')
def user_enters(username):
    print(f" Shalom {username}! ")
    users[username] = request.sid
    
@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)