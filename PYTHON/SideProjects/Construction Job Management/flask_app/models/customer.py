from flask_app.config.mysqlconnection import connectToMySQL

class Customer:
    def __init__(self, data):
        self.id = data['id']
        self.display_name = data['display_name']
        self.notes = data['notes']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO customers (display_name , customers.notes, first_name, last_name, phone, email, address, city, state, zip_code) VALUES (%(display_name)s , %(notes)s , %(first_name)s, %(last_name)s, %(phone)s, %(email)s, %(address)s, %(city)s, %(state)s, %(zip_code)s) JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id INSERT INTO;"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM customers JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id WHERE customers.id = %(customers.id)s;"
        result = connectToMySQL('projects_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM customers JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id WHERE user_id = %(user_id)s"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE customers JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id SET display_name=%(display_name)s, first_name=%(first_name)s , last_name=%(last_name)s , address=%(address)s , city=%(city)s , state=%(state)s , zip_code=%(zip_code)s , customers.notes=%(notes)s, customers.updated_at=NOW() , addresses.updated_at=NOW() , contacts.updated_at=NOW() WHERE customers.id = %(id)s;"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM customers WHERE id = %(id)s;"
        return connectToMySQL('projects_schema').query_db( query, data)