from app import APP
from flask import render_template, redirect, request, session, flash
from app.models import like_model

@APP.route("/dm/<int:message_id>", methods=['POST'])
def like_unlike_message(message_id):
    # check to see message is liked by user already from the db
    # be sure to pass in user and message id!
    like_model.Like.like_message(message_id, session['user_id'])
    return redirect('/dashboard')
    
    

# @APP.route("/")



# @APP.route("/")


# @APP.route("/")


# @APP.route("/")