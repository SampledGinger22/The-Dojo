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
        query = "SELECT * FROM customers WHERE id = %(id)s;"
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
        query = "SELECT * FROM customers WHERE display_name = %(display_name)s and user_id=%(user_id)s;"
        result = connectToMySQL(DATABASE).query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def update_get_disp(cls, data):
        query = "SELECT * FROM customers WHERE display_name = %(display_name)s AND NOT id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db( query , data )
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM customers WHERE user_id = %(user_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_primary(cls, data):
        query = "SELECT * FROM customers LEFT JOIN contacts ON contacts.customer_id = customers.id WHERE user_id=%(user_id)s and contacts.title_id=1;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def get_all_proj(cls, data):
        query = "SELECT * FROM customers LEFT JOIN projects ON projects.customer_id = customers.id WHERE user_id=%(user_id)s and projects.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE customers SET display_name=%(display_name)s, notes=%(notes)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

# DELETION PROCESS

    # @classmethod
    # def delete_cust_contacts(cls, data):
    #     query = "DELETE FROM contacts WHERE customer_id=%(customer_id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete_cust_address(cls, data):
    #     query = "DELETE FROM addresses WHERE customer_id=%(customer_id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete_proj_address(cls, data):
    #     query = "DELETE FROM addresses WHERE project_id=%(project_id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def delete_cust_project(cls, data):
    #     query = "DELETE FROM projects WHERE customer_id=%(customer_id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

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

    @staticmethod
    def validate_update(disp_name):
        is_valid = True
        if Customer.update_get_disp(disp_name):
            flash('Display Name Already In Use')
            is_valid = False
        return is_valid