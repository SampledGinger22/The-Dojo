from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.customer import Customer
from flask_app.models.project import Project
from flask_app.models.contact import Contact
from flask_app.models.address import Address

@app.route('/projects/dash')
def project_dash():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'project_id': Project.id
    }
    context = {
    'project' : Project.get_all(),
    'contact' : Contact.get_by_project(data),
    'address' : Address.get_one_by_project(data)
    }
    return render_template('dash_projects', **context)

@app.route('/projects/<int:id>')
def view_project(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id': id
    }
    projects = Project.get_one(data)
    return render_template('view_project.html', project = projects)

@app.route('/projects/edit/<int:id>')
def edit_project(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id' : id
    }
    projects = Project.get_one(data)
    return render_template('view_project.html', project = projects)

@app.route('/projects/edit/commit', methods=['POST'])
def commit_project():
    data = {
        **request.form
    }
    Project.update(data)
    return redirect('projects/<int:id>')

@app.route('/projects/new')
def new_project():
    if "user_id" not in session:
        return redirect('/login')
    return render_template('new_project.html')

@app.route('/projects/new/commit', methods=['POST'])
def new_project_commit():
    data = {
        **request.form
    }
    Project.save(data)

