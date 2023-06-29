from app.config.mysqlconnection import connectToMySQL

class Message:
    db = chat_db

    def __init__(self, ms_data):
        self.message_id = ms_data['message_id']
        self.content = ms_data['content']
        self.sender_person_id = ms_data['sender_person_id']
        self.receiver_person_id = ms_data['receiver_person_id']
        self.created_at = ms_data['created_at']
        self.updated_at = ms_data['updated_at']

    def __repr__(self) -> str:
        return f'REPR Method {self.message_id}, {self.sender_person_id}, {self.receiver_person_id}'
    
    @classmethod
    def create_message(cls):
        pass
    
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
    
    
    
    
# should I include room id?