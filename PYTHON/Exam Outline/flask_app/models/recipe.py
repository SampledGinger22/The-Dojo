from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instruction']
        self.date_made = data['date_made']
        self.thirty_minutes = data['thirty_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_recipies(cls, data):
        query = "SELECT * FROM recipies"
        return connectToMySQL('recipe').query_db( query, data)

    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipies ( name , description , instructions , date_made , thirty_minutes , created_at, updated_at, user_id) VALUES ( %(name)s , %(description)s , %(instructions)s , %(date_made)s , %(thirty_minutes)s , NOW() , NOW() ) , %(user_id)s;"
        return connectToMySQL('recipe').query_db( query, data )

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipies WHERE id = %(id)s;"
        result = connectToMySQL('recipe').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipies SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, thirty_minutes=%(thirty_minutes)s updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipe').query_db(query,data)
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipies WHERE id = %(id)s;"
        return connectToMySQL('recipe').query_db( query, data)