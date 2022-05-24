from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Project:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.customer_id = data['customer_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO projects (name , start_date, end_date, project_notes, customer_id) VALUES (%(name)s, %(start_date)s, %(end_date)s, %(project_notes)s, %(customer_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM projects JOIN customers ON customer_id = customers.id JOIN addresses ON addresses.project_id = projects.id JOIN contacts ON contacts.project_id = projects.id WHERE user_id = %(user_id)s and projects.id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM projects JOIN addresses ON addresses.project_id = projects.id JOIN contacts ON contacts.project_id = projects.id;"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def get_by_customer(cls, data):
        query = "SELECT * FROM projects WHERE customer_id = %(customer_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_name(cls, data):
        query = "SELECT * FROM projects WHERE name=%(name)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_name(cls, data):
        query = "SELECT * FROM projects WHERE name = %(name)s;"
        result = connectToMySQL(DATABASE).query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE projects SET name=%(name)s, start_date=%(start_date)s, end_date=%(end_date)s, customer_id=%(customer_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    
    @staticmethod
    def validate(name):
        is_valid = True
        if Project.get_name(name):
            flash('Name Already In Use')
            is_valid = False
        return is_valid