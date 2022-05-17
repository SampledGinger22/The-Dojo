from flask_app.config.mysqlconnection import connectToMySQL

class Project:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.customer_id = data['customer_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO projects (name , start_date, end_date, customer_id) VALUES (%(name)s, %(start_date)s, %(end_date)s, %(customer_id)s);"
        return connectToMySQL('projects').query_db(cls, data)

# UPDATE SCHEMA THROUGHOUT DOCUMENTS / CORRECT 'PROJECTS' THROUGHOUT THIS, CUSTOMER, CONTACT, AND ADDRESS. PICK UP UNDER THIS.

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM projects JOIN addresses ON addresses.customer_id = projects.id JOIN contacts ON contacts.customer_id = projects.id WHERE id = %(id)s;"
        result = connectToMySQL('projects').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "GET * FROM projects JOIN addresses ON addresses.customer_id = projects.id JOIN contacts ON contacts.customer_id = projects.id"
        return connectToMySQL('projects').query_db(cls, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE projects SET display_name=%(display_name)s, notes=%(notes)s;"
        return connectToMySQL('projects').query_db(cls, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL('projects').query_db( query, data)