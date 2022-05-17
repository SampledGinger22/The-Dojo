from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.project import Project
from flask_app.models.contact import Contact
from flask_app.models.address import Address

@app.route('/projects/dash')
def project_dash():
    data = {
        'project_id': Project.id
    }
    context = {
    'projects' : Project.get_all(),
    'contacts' : Contact.get_by_project(data),
    'addresses' : Address.get_one_by_project(data)
    }
    return render_template('dash_projects', **context)

@app.route('/projects/<int:id>')
def view_project(id):
    data = {
        'id': id
    }
    projects = Project.get_one(data)
    return render_template('view_project.html', project = projects)

@app.route('/projects/edit/<int:id>')
def edit_project(id)
    data = {
        'id' : id
    }
    projects = Project.get_one(data)
    return render_template('view_project.html', project = projects)

@app.route('/projects/edit/commit', methods=('POST'))