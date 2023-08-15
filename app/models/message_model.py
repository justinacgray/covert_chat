from app.config.mysqlconnection import MySQLConnection, connectToMySQL
from uuid import uuid4
import random
from flask import flash, session
from app.models import person_model, message_model
from pprint import pprint

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
        self.liked_by = []
        
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
    
    
    # todo amend query below to includes likes to use that attribute length in the HTMl 
    @classmethod
    def read_all_messages_by_receiver(cls, sender_id, receiver_id):
                    # left side 'user_id' needs to match %(user_id)s
        user_data_dict = {
                        'user_id' : sender_id,
                        'other_user_id' : receiver_id
                        }
        all_messages = []
        query = '''
            select m.*,
            sender.username AS sender_name,
            receiver.username AS receiver_name,
            likes.liked_by_user_id
            FROM messages AS m
            LEFT JOIN persons AS sender ON m.sender_user_id = sender.user_id
            LEFT JOIN persons AS receiver ON m.receiver_user_id = receiver.user_id
            LEFT JOIN likes ON m.message_id = likes.message_id
            WHERE (m.sender_user_id = %(user_id)s  and m.receiver_user_id = %(other_user_id)s )
            or (m.sender_user_id = %(other_user_id)s  and m.receiver_user_id = %(user_id)s  )
            ;
        '''
        results = MySQLConnection(cls.db).query_db(query, user_data_dict)
        pprint(results, width=1, sort_dicts=False)
        # this for scalability 
        # handles cases where the same message might appear multiple times due to being 
        # associated with different likes.
        for row in results:
            # if message is new - no duplicates
                                # last item added 
            if (len(all_messages) == 0) or (row['message_id'] !=  all_messages[-1].message_id):
                one_message = cls(row)
                # append the user ids to the liked_by_user list
                if row['liked_by_user_id'] is not None:
                    one_message.liked_by.append(row['liked_by_user_id'])
                # finally always append the message- doesn't matter if conditional is true or not
                all_messages.append(one_message)
            # if message is duplicated 
            else:
                one_message.liked_by.append(row['liked_by_user_id'])

            
        print("all messages by receiver ----->", all_messages)
        return all_messages
        
        
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
            select p.*
            from persons p
            join messages m 
            on (m.sender_user_id = %(user_id)s AND m.receiver_user_id = p.user_id)
            OR (m.receiver_user_id = %(user_id)s AND m.sender_user_id = p.user_id)
            group by p.user_id
            ;
        '''
        results = MySQLConnection(cls.db).query_db(query, user_data)
        print("USER chats --->", user_data)
        print("****** RESULTS *****", results)
        chat_list = []
        for row in results:
            chat_list.append(person_model.Person(row))
        print("$$$$$$$ chat list $$$$$", chat_list)
        return chat_list
    
    
# should I include room id?