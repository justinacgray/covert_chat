from app.config.mysqlconnection import connectToMySQL

class Group:
    db = chat_db

    def __init__(self, room_data):
        self.room_id = room_data['room_id']
        self.title = room_data['title'] 
        self.creator_user_id = room_data['creator_user_id']
        self.created_at = room_data['created_at']
        self.updated_at = room_data['updated_at']
        self.messages = []

    @classmethod
    def hello(cls):
        pass
    
    @classmethod
    def create_group(cls):
        pass
    

    @classmethod
    def read_all_messages_in_group(cls):
        pass
    
    @classmethod
    def update_message_in_group(cls):
        pass
    
    @classmethod
    def delete_message_in_group(cls):
        pass
    


class GroupMembers:
    pass

# should I include messages_id?