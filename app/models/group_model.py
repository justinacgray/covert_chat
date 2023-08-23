from app.config.mysqlconnection import MySQLConnection, connectToMySQL
import random
from flask import flash, session

db = 'chat_db'

class Group:
    def __init__(self, room_data):
        self.group_id = room_data['group_id']
        self.group_name = room_data['group_name'] 
        self.created_at = room_data['created_at']
        self.updated_at = room_data['updated_at']
        self.creator_user_id = room_data['creator_user_id']
        self.group_members = []

    
    @classmethod
    def create_group(cls, group_data):
        if not cls.valid_group(group_data):
            return False
        
        parsed_group_dict = cls.parse_group_data(group_data)
        query = '''
            INSERT INTO `groups` (group_id, group_name, creator_user_id )
            VALUES ( %(group_id)s, %(group_name)s, %(creator_user_id)s);
        '''
        
        results = MySQLConnection(db).query_db(query, parsed_group_dict)
        print("RESULTS group_data ====> ", results)
        new_group_id = parsed_group_dict['group_id']
        print("NEW GROUP DATA ====>", new_group_id)
        return new_group_id
    

    @classmethod
    def read_all_messages_in_group(cls):
        pass
    
    @classmethod
    def update_message_in_group(cls):
        pass
    
    @classmethod
    def delete_message_in_group(cls):
        pass
    
    
    @staticmethod
    def valid_group(group_dict):
        is_valid =True
        if len(group_dict["group_name"]) < 2:
            flash( "Group Name must be at least 2 characters", category='error')
            print("group name error")
            is_valid = False
        return is_valid
    
    @staticmethod
    def parse_group_data(group_data):
        parsed_data = {
            'group_id' : random.getrandbits(22),
            'group_name' : group_data['group_name'],
            'creator_user_id' : group_data['creator_user_id']
        }
        print("$$$$$$$$$$$$$ parsed group data ===>" , parsed_data)
        return parsed_data 

class GroupMembers:
    def __init__(self, group_members_data):
        self.group_id = group_members_data['group_id']
        self.group_name = group_members_data['group_name']
        self.persons_user_id = group_members_data['persons_user_id']
        self.created_at = group_members_data['created_at']
        self.updated_at = group_members_data['updated_at']
        
    @classmethod
    def create_members_per_group(cls, group_id, user_id ):
        group_members = {
            "group_id" : group_id,
            "persons_user_id" : user_id
        }
        query = '''
            INSERT INTO `group_members` (group_id, persons_user_id )
            VALUES ( %(group_id)s, %(persons_user_id)s);
        '''
        results = MySQLConnection(db).query_db(query, group_members)
        print("RESULTS group_members ====> ", results)
        
        return results