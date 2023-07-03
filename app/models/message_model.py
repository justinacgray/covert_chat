from app.config.mysqlconnection import connectToMySQL
from uuid import uuid4

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
    def create_message(cls):
        # query ='''
        #         INSERT into messages (message_id, content, ) 
        #         VALUES ( %(message_id)s, %(content)s, %()s, %()s, %()s, %()s )
        #         ;
        #         '''
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
    def parse_id_data(data):
        parsed_data = {
            'id': uuid4().hex
        }
        print("$$$$$$$$$$$$$ parsed user data ===>" , parsed_data)
        return parsed_data
    
    @staticmethod
    def valid_message(data):
        pass
    
# should I include room id?