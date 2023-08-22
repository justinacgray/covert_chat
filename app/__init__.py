from flask import Flask
import os
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
load_dotenv()


APP = Flask(__name__)
socketio = SocketIO(APP)
FLASK_SECRET = os.getenv('FLASK_SECRET')



APP.secret_key = FLASK_SECRET


print("inside the init file")


