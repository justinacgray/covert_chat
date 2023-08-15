from app.config.mysqlconnection import MySQLConnection, connectToMySQL
from app.models import message_model


class Like:
    db = 'chat_db'

    def __init__(self, like_data):
        self.message_id = like_data['message_id']
        self.liked_by_user_id = like_data['like_by_user_id']
        
    @classmethod
    def like_message(cls, message_id, user_id):
        message_dict = {
                        'message_id' : message_id,
                        'logged_in_user_id' : user_id
                        }
        # if message is liked by this user return ...
        print('---> LIKE MESSAGE DICT -----> ', message_dict)
        if cls.checked_if_user_liked_message(message_id, user_id):
            query = """  
                DELETE FROM likes
                WHERE message_id = %(message_id)s
                ;"""
            result= MySQLConnection(cls.db).query_db(query, message_dict)
            return result
        
        query = '''
            INSERT INTO likes (message_id, liked_by_user_id)
            VALUES ( %(message_id)s, %(logged_in_user_id)s );
        '''
        results = MySQLConnection(cls.db).query_db(query, message_dict)
        print("RESULTS FROM LIKE", results)
        
        return results
        

    @classmethod
    def checked_if_user_liked_message(cls, message_id, user_id):
        message_dict = {
                        'message_id' : message_id,
                        'logged_in_user_id' : user_id
                        }
        query = '''
            SELECT *
            FROM likes
            WHERE message_id = %(message_id)s
            and liked_by_user_id = %(logged_in_user_id)s
            ;        
        '''
        results = MySQLConnection(cls.db).query_db(query, message_dict)
        print("RESULTS FROM LIKE", results)
        
        return results
    
    @classmethod
    def get_all_likes_by_message_id(cls, message_id):
        message_dict = {
                    'message_id' : message_id
        }
        query = '''
            SELECT *
            FROM likes
            WHERE message_id = %(message_id)s;        
        '''
        likes_list = []
        results = MySQLConnection(cls.db).query_db(query, message_dict)
        print("RESULTS FROM LIKE", results)
        for row in results:
            one_like = cls(row)
            likes_list.append(one_like)
        return likes_list
    
    