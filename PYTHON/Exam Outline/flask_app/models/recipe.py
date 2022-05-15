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
    def get_all_recipies(cls):
        query = "SELECT * FROM recipies"
        return connectToMySQL('recipe').query_db(query)

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

    @staticmethod
    def recipe_entry_val(recipe):
        is_valid = True
        if len(recipe['name']) > 0:
            flash("Recipe must have a name!")
            is_valid = False
        if len(recipe['description']) > 0:
            flash("Recipe must have a description!")
            is_valid = False
        if not (recipe['instructions']) > 0:
            flash('Recipe must have instructions!')
            is_valid = False
        if not (recipe['date_made']):
            flash('You must enter a date made on!')
            is_valid = False
        if not (recipe['under_thirty']):
            flash('you must select if this takes less than thirty minutes!')
            is_valid = False
        return is_valid

    @staticmethod
    def recipe_length_val(recipe):
        is_valid = True
        if len(recipe['name']) <= 3:
            flash("Recipe name must be at least 3 characters long.")
            is_valid = False
        if len(recipe['description']) <= 3:
            flash("Recipe name must be at least 3 characters long.")
            is_valid = False
        if not (recipe['instructions']) <= 3:
            flash('Recipe name must be at least 3 characters long.')
            is_valid = False
        return is_valid