from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/newrecipe')
def new_recipe():
    return render_template("new_recipe.html")

@app.route('/saverecipe', methods=["POST"])
def save_recipe():
    data = {
        'user_id': session['user_id']
        **request.form
    }
    if not Recipe.recipe_length_val(request.form):
        return redirect('/newrecipe')
    if not Recipe.recipe_entry_val(request.form):
        return redirect('/newrecipe')
    Recipe.save_recipe(data)
    return redirect('/user_dash')

@app.route('/viewrecipe/<int:id>')
def view_recipe(id):
    data = {
        'id':id
    }
    recipe = Recipe.get_recipe(data)
    print(recipe)
    return render_template('view_recipe.html', recipes = recipe)

@app.route('/recipe/<int:id>/edit')
def edit(id):
    data = {
        'id' : id
            }
    return render_template('edit_recipe.html', recipies = Recipe.get_recipe(data))

@app.route('/updaterecipe/<int:id>', methods = ["POST"])
def update(id):
    data = {
        'id':id,
        **request.form
    }
    if not Recipe.recipe_length_val(request.form):
        return redirect('/recipe/<int:id>/edit')
    if not Recipe.recipe_entry_val(request.form):
        return redirect('/recipe/<int:id>/edit')
    Recipe.update_recipe(data)
    return redirect('/user_dash')

@app.route('/recipe/<int:id>/destroy')
def delete_recipe(id):
    data = {
        'id' : id
            }
    Recipe.delete(data)
    return redirect('/user_dash')