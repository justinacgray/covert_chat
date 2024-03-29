from app.config.mysqlconnection import MySQLConnection, connectToMySQL
from uuid import uuid4
from app import APP
from flask import flash, session
import re
import random
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(APP)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Person:
    db = 'chat_db'
    
    def __init__(self, p_data):
        self.user_id = p_data['user_id']
        self.first_name = p_data['first_name']
        self.last_name = p_data['last_name']
        self.username = p_data['username']
        self.age = p_data['age']
        self.email = p_data['email']
        self.password = p_data['password']
        self.created_at = p_data['created_at']
        self.updated_at = p_data['updated_at']
        self.active_chats = []

        
    def __repr__(self) -> str:
        return f"PERSON USER ===> : {self.first_name, self.last_name, self.email}"
    
    # create user 
    @classmethod
    def create_user(cls,data):
        # if not User.valid_register_data OR
        if not cls.valid_register_data(data):
            return False
        # why do we need this parsed data?
        # why only parsing email and password?
        parsed_data = cls.parse_registration_data(data)
        query = """
            INSERT INTO persons (user_id, first_name, last_name, username, age, email, password) 
            VALUES ( %(id)s, %(first_name)s, %(last_name)s, %(username)s, %(age)s, %(email)s, %(password)s )
            ;"""

        user_id = connectToMySQL(cls.db).query_db(query, parsed_data)
        if str(user_id) == "False":
            return False
        session['user_id'] = parsed_data['id']
        session['username'] = parsed_data['username']

        print("SESSION ===>", session)
        print("USER ID FROM MODELS ==>", user_id)
        return True
    
            
    
    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * FROM persons
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        # print("********result *********", result)
        users = []
        for row in result:
            users.append(cls(row))
        # print("************ users ===>", users)
        return users
    
    @classmethod
    def get_user_by_id(cls, curr_user_id):
        data = { 'id' : curr_user_id}
        query = """
        SELECT * 
        FROM users
        WHERE user_id = %(user_id)s
        ;"""
        result= connectToMySQL(cls.db).query_db(query,data)
        # print("===> user result ===>", result)
        return result
    
    # eventually be able to update user profile
    @classmethod
    def update_user(cls):
        pass
    
    @classmethod
    def delete_user(cls):
        pass
    
    @classmethod
    def get_user_by_email(cls, email):
        data = {"email" : email}
        query= """
        SELECT * 
        FROM persons
        WHERE email = %(email)s
        ;"""
        result = MySQLConnection(cls.db).query_db(query, data)
        if result:
            # this means the first result in the result
            result = cls(result[0])
        print("user result ===> ", result)
        return result
        
    # validate 
    @staticmethod
    def valid_register_data(register_data):
        is_valid = True
        
        # checking if email exits and anything the user enters it lowercases
        current_user = Person.get_user_by_email(register_data['email'].lower())
        print("current user===>", current_user)
    
        if current_user:
            flash("That email is already in use", category='error')
            print("This user exists")
            is_valid = False
        # data needs to be wrapped in parenthesis in order for it to be read
        if len(register_data["first_name"].strip()) < 2:
            flash( "First Name must be at least 2 characters", category='error')
            print("first name error")
            is_valid = False
            
        #length of the last name
        if len(register_data["last_name"].strip()) < 2:
            flash("Last Name ust be at least 2 characters", category='error')
            print("last name error")
            is_valid = False
            
        #length of age 
        if len(register_data["age"].strip()) == 0:
            flash("Age mst be entered", category='error')
            print("age error")
            is_valid = False
            
        #email matches format
        if not EMAIL_REGEX.match(register_data['email']):    # test whether a field matches the pattern            
            flash("invalid email address!", category='error')
            print("email not valid error")
            is_valid = False
            
        #password was entered was less than 8
        if len(register_data['password'].strip()) < 8:
            flash("Password must be minimum 8 characters", category='error')
            print("password error")
            is_valid = False
            
        # password and confirm password must match 
        if (register_data['password'].strip() != register_data['confirm_password'].strip()):
            flash("Passwords do not match", category='error')
            print("passwords do not match error")
            is_valid = False
        print("completed register validations")
        return is_valid
    
    
    @staticmethod
    def valid_login_data(login_data):
        is_valid = True
        
        # add logic to login either email or username
        user = Person.get_user_by_email(login_data['email'].lower())
        if user:
            if bcrypt.check_password_hash(user.password, login_data['password']):
                session['user_id'] = user.user_id
                session['username'] = user.username         
                return True
            else:
                flash("Login credentials are incorrect", category='error')
                return False
        if not user:
            flash('User does not exist', category='error')
            return False
        
        if len(login_data['email'].strip()) == 0:
            flash("Email must be entered", category='error')
            is_valid = False
            
        if len(login_data['password'].strip()) == 0:
            flash("Password must be entered", category='error')
            is_valid = False
        print("completed login validations")
        return is_valid


    @staticmethod
    def parse_registration_data(data):
        parsed_data = {
            # 'id': uuid4().hex,
            'id' : random.getrandbits(22),
            'first_name' : data['first_name'],
            'last_name' : data['last_name'],
            'username' : data['username'],
            'age' : data['age'],
            'email' : data['email'].lower(), 
            'password' : bcrypt.generate_password_hash(data['password'])
        }
        print("$$$$$$$$$$$$$ parsed user data ===>" , parsed_data)
        return parsed_data 








print("inside person model")