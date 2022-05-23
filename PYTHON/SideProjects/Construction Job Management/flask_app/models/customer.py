from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Customer:
    def __init__(self, data):
        self.id = data['id']
        self.display_name = data['display_name']
        self.notes = data['notes']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO customers (display_name , notes, user_id) VALUES (%(display_name)s, %(notes)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM customers LEFT JOIN addresses ON addresses.customer_id = customers.id LEFT JOIN contacts ON contacts.customer_id = customers.id LEFT JOIN projects ON projects.customer_id = customers.id JOIN titles ON contacts.title_id = titles.id WHERE contacts.customer_id = %(customer_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_disp(cls, data):
        query = "SELECT * FROM customers WHERE display_name = %(display_name)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_disp(cls, data):
        query = "SELECT * FROM customers WHERE display_name = %(display_name)s;"
        result = connectToMySQL(DATABASE).query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM customers LEFT JOIN contacts ON contacts.customer_id = customers.id LEFT JOIN projects ON projects.customer_id = customers.id WHERE user_id = %(user_id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE customers JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id SET display_name=%(display_name)s, first_name=%(first_name)s , last_name=%(last_name)s , address=%(address)s , city=%(city)s , state=%(state)s , zip_code=%(zip_code)s , customers.notes=%(notes)s, customers.updated_at=NOW() , addresses.updated_at=NOW() , contacts.updated_at=NOW() WHERE customers.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM customers WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    @staticmethod
    def validate(disp_name):
        is_valid = True
        if Customer.get_disp(disp_name):
            flash('Display Name Already In Use')
            is_valid = False
        return is_valid
