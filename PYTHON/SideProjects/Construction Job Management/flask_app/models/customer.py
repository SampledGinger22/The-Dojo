from flask_app.config.mysqlconnection import connectToMySQL

class Customer:
    def __init__(self, data):
        self.id = data['id']
        self.display_name = data['display_name']
        self.notes = data['notes']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO customers (display_name , notes) VALUES (%(display_name)s , %(notes)s);"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM customers WHERE id = %(id)s;"
        # JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id
        result = connectToMySQL('projects_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "GET * FROM customers WHERE user_id = %(user_id)s"
        # JOIN addresses ON addresses.customer_id = customers.id JOIN contacts ON contacts.customer_id = customers.id
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE customers SET display_name=%(display_name)s, notes=%(notes)s, updated_at=NOW();"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM customers WHERE id = %(id)s;"
        return connectToMySQL('projects_schema').query_db( query, data)