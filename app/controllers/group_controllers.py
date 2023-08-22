from app import APP
from flask import render_template, redirect, request, session, flash
from app import socketio
from flask_socketio import SocketIO, emit



@APP.route("/group-chat")
def render_group_chat(): 
    return render_template('group_chat.html')


@socketio.on('group-msgs')
def enter_group(data):
    print('shalom' + data)
    emit('joined_group', {'message': 'You have joined the group chat.'})


@socketio.on('group-msgs')
def enter_group(data):
    print('shalom' + data)
    emit('group-msgs', {'message': 'You have joined the group chat.'})




# @APP.route("/")


# @APP.route("/")


# @APP.route("/")