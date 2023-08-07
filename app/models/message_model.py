from app.config.mysqlconnection import MySQLConnection, connectToMySQL
from uuid import uuid4
import random
from flask import flash, session
from app.models import person_model, message_model


class Message:
    db = 'chat_db'

    def __init__(self, ms_data):
        # html side          database values/fields  
        self.message_id = ms_data['message_id']
        self.content = ms_data['content']
        self.sender_person_id = ms_data['sender_user_id']
        self.receiver_person_id = ms_data['receiver_user_id']
        self.created_at = ms_data['created_at']
        self.updated_at = ms_data['updated_at']
        self.sender_obj = None
        self.receiver_obj = None
        
    def __repr__(self) -> str:
        return f'REPR MESSAGE Method id: {self.message_id}, sender:{self.sender_person_id}, receiver:{self.receiver_person_id}'
    
    # use sql alchemy to CRUD
    @classmethod
    def create_message(cls, msg_data):
        parsed_data = cls.parse_msg_data(msg_data)
        query ='''
                INSERT into messages (message_id, content, receiver_user_id, sender_user_id) 
                VALUES ( %(message_id)s, %(content)s, %(receiver_user_id)s, %(sender_user_id)s)
                ;'''
        message_id = connectToMySQL(cls.db).query_db(query, parsed_data)
        if str(message_id) == 'False':
            return False
        print("message created id", message_id)
        return True
    
    @classmethod
    def read_one_message(cls):
        pass
    
    @classmethod
    def read_all_messages(cls):
        pass
    
    @classmethod
    def update_message(cls):
        pass
    
    @classmethod
    def delete_message(cls):
        pass
    
    
    # parse message_id
    @staticmethod
    def parse_msg_data(msg_data):
        print("<----- MSG data ---->", msg_data)
        # left side matches db
        parsed_data = {
            'message_id': random.getrandbits(22),
            'content' : msg_data['content'],
            'sender_user_id' : session['user_id'],
            'receiver_user_id' : msg_data['receiver_person_id'],
        }
        
        return parsed_data
    
    @staticmethod
    def valid_message(msg_content):
        print("**** MSG content ***", msg_content)
        print("--> Receiver person -->", msg_content['receiver_person_id'])
        
        is_valid = True
        if int(msg_content['receiver_person_id']) == 0:
            flash("please choose a person to message")
            is_valid = False
        # == 0 must go OUTSIDE of the len function
        if len(msg_content['content']) == 0:
            flash("content can't empty")
            is_valid = False
            
        return is_valid
    
    
    @classmethod
    def logged_in_user_active_chats(cls, user_id):
        user_data = {
            'user_id' : user_id
        }
        query = '''
            SELECT m.*,
            sender.username AS sender_name,
            receiver.username AS receiver_name
            FROM messages AS m
            LEFT JOIN persons AS sender ON m.sender_user_id = sender.user_id
            LEFT JOIN persons AS receiver ON m.receiver_user_id = receiver.user_id
            WHERE sender.user_id = %(user_id)s OR receiver.user_id = %(user_id)s
            -- GROUP BY m.receiver_user_id, m.sender_user_id
        
            ;
        '''
        results = MySQLConnection(cls.db).query_db(query, user_data)
        print("USER chats --->", user_data)
        print("****** RESULTS *****", results)
        chat_list = []
        for row in results:
            messages = cls(row)
            sender_user_data = {
                'user_id' : row['sender_user_id'],
                'first_name' : None,
                'last_name': None,
                'username' : row['sender_name'],
                'age' : None,
                'email' : None,
                'password' : None,
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            receiver_user_data = {
                'user_id' : row['receiver_user_id'],
                'first_name' : None,
                'last_name': None,
                'username' : row['receiver_name'],
                'age' : None,
                'email' : None,
                'password' : None,
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            sender_person = person_model.Person(sender_user_data)
            receiver_person = person_model.Person(receiver_user_data)
            messages.sender_obj = sender_person
            messages.receiver_obj = receiver_person
            chat_list.append(messages)
        print("$$$$$$$ chat list $$$$$", chat_list)
        return chat_list
    
    
# should I include room id?