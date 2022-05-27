from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Address:
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address'] 
        self.city = data['city']
        self.state = data['state']
        self.zip_code = data['zip_code']
        self.project_id = data['project_id']
        self.customer_id = data['customer_id']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO addresses ( address, city, state, zip_code, created_at, updated_at, project_id, customer_id) VALUES (%(address)s , %(city)s , %(state)s , %(zip_code)s , %(created_at)s , %(updated_at)s , %(project_id)s , %(customer_id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def save_with_customer(cls, data):
        query = 'INSERT INTO addresses ( address, city, state, zip_code, created_at, updated_at , customer_id) VALUES (%(address)s , %(city)s , %(state)s , %(zip_code)s , NOW() , NOW() , %(customer_id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def save_with_project(cls, data):
        query = 'INSERT INTO addresses ( address, city, state, zip_code, project_id) VALUES (%(address)s, %(city)s , %(state)s , %(zip_code)s, %(project_id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_by_project(cls, data):
        query = "SELECT * FROM addresses WHERE project_id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])
    
    @classmethod
    def get_one_by_customer(cls, data):
        query = "SELECT * FROM addresses WHERE customer_id = %(id)s;"
        result =  connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE addresses SET address=%(address)s, city=%(city)s, state=%(state)s, zip_code=%(zip_code)s, updated_at=NOW(), project_id=%(project_id)s, customer_id=%(customer_id)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_with_cust(cls, data):
        query = "UPDATE addresses SET address=%(address)s, city=%(city)s, state=%(state)s, zip_code=%(zip_code)s, updated_at=NOW() WHERE customer_id=%(customer_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update_with_project(cls, data):
        query = "UPDATE addresses SET address=%(address)s, city=%(city)s, state=%(state)s, zip_code=%(zip_code)s, updated_at=NOW() WHERE project_id=%(project_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM addresses WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete_cust_address(cls, data):
        query = "DELETE FROM addresses WHERE customer_id=%(customer_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_cust_proj_address(cls, data):
        query = "DELETE FROM addresses LEFT JOIN projects ON projects.id = addresses.project_id WHERE projects.customer_id=%(customer_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_proj_address(cls, data):
        query = "DELETE FROM addresses WHERE project_id=%(project_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(address):
        is_valid = True
        if len(address['address']) < 3:
            flash("Must be valid address", "address_valid")
            is_valid = False
        if len(address['city']) < 2:
            flash("Must be valid city", "city_valid")
            is_valid = False
        if not(address['city']).isalpha():
            flash("City must be valid", "city_alpha")
            is_valid = False
        if not len(address['state']) == 2:
            flash("State abbreviation must be valid", "state_valid")
            is_valid = False
        if not(address['state']).isalpha():
            flash("State must be valid", "state_alpha")
            is_valid = False
        if not len(address['zip_code']) == 5:
            flash("Zip code must be five numbers in length", "zip_code_valid")
            is_valid = False
        if not(address['zip_code']).isnumeric():
            flash("Must be valid zip code", "zip_numeric")
            is_valid = False
        return is_valid
