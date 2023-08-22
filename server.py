from app import APP
from app import socketio
from app.controllers import person_controllers, message_controllers, like_controllers, group_controllers





print("inside server")

if __name__ == "__main__":
    socketio.run(APP, debug=True)
    # APP.run(debug=True)