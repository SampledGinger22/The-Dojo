from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Title:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM titles;"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM titles WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)