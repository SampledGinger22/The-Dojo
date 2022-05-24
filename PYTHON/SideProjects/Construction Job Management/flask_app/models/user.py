from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import DATABASE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , password , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users Set first_name=%(first_name)s, last_name==%(last_name)s, email==%(email)s, updated_at=NOW();"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not user['first_name'].isalpha():
            flash('First name must only contain letters!')
            is_valid = False
        if not user['last_name'].isalpha():
            flash('Last name must only contain letters!')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address')
            is_valid = False
        if User.get_by_email(user):
            flash('This email is already in use')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if not user['conf_password'] == user['password']:
            flash('Passwords do not match!')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address')
            is_valid = False
        return is_valid
