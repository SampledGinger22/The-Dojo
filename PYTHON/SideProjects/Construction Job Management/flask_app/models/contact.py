from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$') 

class Contact:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone = data['phone']
        self.email = data['email']
        self.notes = data['notes']
        self.customer_id = data['customer_id']
        self.project_id = ['project_id']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO contacts ( first_name , last_name , phone , email , notes , customer_id , project_id , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(phone)s , %(email)s , %(notes)s , %(customer_id)s , %(project_id)s , NOW() , NOW() );"
        return connectToMySQL('projects_schema').query_db( query, data )

    @classmethod
    def get_by_customer(cls, data):
        query = "SELECT * FROM contacts WHERE customer_id = %(customer_id)s;"
        result = connectToMySQL('projects_schema').query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_by_project(cls, data):
        query = "SELECT * FROM contacts WHERE project_id = %(project_id)s;"
        result = connectToMySQL('projects_schema').query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM contacts WHERE id = %(id)s;"
        result = connectToMySQL('projects_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE contacts SET first_name=%(first_name)s, last_name=%(last_name)s, phone=%(phone)s, email=%(email)s, notes=%(notes)s, updated_at=NOW(), customer_id=%(customer_id)s, project_id=%(project_id)s;"
        return connectToMySQL('projects_schema').query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM contacts WHERE id = %(id)s;"
        return connectToMySQL('projects_schema').query_db( query, data)

    @staticmethod
    def validate(contact):
        is_valid = True
        if len(contact['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if not (contact['first_name']).isalpha():
            flash('First name must only contain letters!')
            is_valid = False
        if len(contact['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not (contact['last_name']).isalpha():
            flash('Last name must only contain letters!')
            is_valid = False
        if not EMAIL_REGEX.match(contact['email']):
            flash('Invalid email address')
            is_valid = False
        return is_valid