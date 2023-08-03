from app.config.mysqlconnection import connectToMySQL
from uuid import uuid4
import random
from flask import flash, session

class Message:
    db = 'chat_db'

    def __init__(self, ms_data):
        self.message_id = ms_data['message_id']
        self.content = ms_data['content']
        self.sender_person_id = ms_data['sender_person_id']
        self.receiver_person_id = ms_data['receiver_person_id']
        self.created_at = ms_data['created_at']
        self.updated_at = ms_data['updated_at']
        self.user_obj = None

    def __repr__(self) -> str:
        return f'REPR Method {self.message_id}, {self.sender_person_id}, {self.receiver_person_id}'
    
    # use sql alchemy to CRUD
    @classmethod
    def create_message(cls, msg_data):
        if not cls.valid_message(msg_data):
            return False
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
        parsed_data = {
            'message_id': random.getrandbits(22),
            'content' : msg_data['content'],
            'sender_person_id' : session['user_id'],
            'receiver_user_id' : msg_data['receiver_person_id'],
        }
        
        return parsed_data
    
    @staticmethod
    def valid_message(msg_content):
        print("msg content", msg_content)
        print("len", len(msg_content['receiver_person_id']))
        print("receiver person", msg_content['receiver_person_id'])
        
        is_valid = True
        if int(msg_content['receiver_user_id']) == 0:
            flash("please choose a person to message")
            is_valid = False
        # == 0 must go OUTSIDE of the len function
        if len(msg_content['content']) == 0:
            flash("content can't empty")
            is_valid = False
            
        return is_valid
    
    
    
    
# should I include room id?