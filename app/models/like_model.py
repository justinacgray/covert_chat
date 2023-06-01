from app.config.mysqlconnection import connectToMySQL

class Like:
    db = chat_db

    def __init__(self, like_data):
        self.like_id = like_data['like_id']
        self.message_id = like_data['message_id']
        self.liked_by_user_id = like_data['like_by_user_id']
        
        self.created_at = like_data['created_at']
        self.updated_at = like_data['updated_at']

    @classmethod
    def hello(cls):
        pass