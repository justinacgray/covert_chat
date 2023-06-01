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

    @classmethod
    def hello(cls):
        pass
    
    
    
# should I include room id?