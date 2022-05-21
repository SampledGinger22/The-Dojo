from types import ClassMethodDescriptorType
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
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM projects JOIN customers ON customer_id = customers.id JOIN addresses ON addresses.project_id = projects.id JOIN contacts ON contacts.project_id = projects.id WHERE user_id = %(user_id)s and projects.id=%(id)s;"
        result = connectToMySQL('projects_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM projects JOIN users ON users.id = projects.user_id JOIN addresses ON addresses.project_id = projects.id JOIN contacts ON contacts.project_id = projects.id WHERE user_id=%(user_id)s;"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def get_by_customer(cls, data):
        query = "SELECT * FROM projects WHERE customer_id = %(customer_id)s"

    @classmethod
    def update(cls, data):
        query = "UPDATE projects SET name=%(name)s, start_date=%(start_date)s, end_date=%(end_date)s, customer_id=%(customer_id)s;"
        return connectToMySQL('projects_schema').query_db(cls, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM projects WHERE id = %(id)s;"
        return connectToMySQL('projects_schema').query_db( query, data)