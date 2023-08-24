
from app import APP, socketio
from flask import render_template, redirect, request, session, flash
from flask_socketio import SocketIO, emit

users = {}


@socketio.on('connect')
def enter_group():
    print('shalom friend')
    

@socketio.on('user_join')
def user_enters(username):
    print(f" Shalom {username}! ")
    users[username] = request.sid