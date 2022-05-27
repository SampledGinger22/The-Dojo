from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.customer import Customer
from flask_app.models.project import Project
from flask_app.models.contact import Contact
from flask_app.models.address import Address
from flask_app.models.title import Title

@app.route('/projects/dash')
def project_dash():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id'],
        'project_id': Project.id
    }
    context = {
    'project' : Project.get_all(data),
    'contact' : Contact.get_by_project(data),
    'address' : Address.get_one_by_project(data)
    }
    return render_template('dash_projects', **context)

# View / Edit

@app.route('/projects/view/<int:id>')
def view_project(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id'],
        'id': id
    }
    context = {
        'project': Project.get_one(data),
        'address': Address.get_one_by_project(data),
        'contacts': Contact.get_by_project(data),
        'customer': Customer.get_all(data),
        'primaries': Contact.get_primary(),
        'owners': Customer.get_all_proj(data)
    }
    return render_template('view_project.html', **context)

@app.route('/projects/edit/<int:id>/commit', methods=["POST"])
def project_edit_commit(id):
    disp_data = {
        'name': request.form['name'],
        'id': id
    }
    if not Project.validate_update(disp_data):
        return redirect(request.referrer)
    data = {
        'id': id,
        **request.form
    }
    Project.update(data)
    Contact.update_cust_id(data)
    address_data = {
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip_code': request.form['zip_code'],
        'project_id': id
    }
    Address.update_with_project(address_data)
    return redirect(request.referrer)

# New Projects

@app.route('/projects/new')
def new_project():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        "user_id": session['user_id']
    }
    context = {
        'customers': Customer.get_all(data),
        'titles': Title.get_all()
    }
    return render_template('new_project.html', **context)

@app.route('/projects/new/commit', methods=['POST'])
def new_project_commit():
    disp_data = {
        'name': request.form['name']
    }
    if not Project.validate(disp_data):
        return redirect(request.referrer)
    project_data = {
        'name': request.form['name'],
        'customer_id': request.form['customer'],
        'project_notes': request.form['project_notes'],
        'start_date': request.form['start_date'],
        'end_date': request.form['end_date']
    }
    Project.save(project_data)
    project_id = Project.get_by_name(disp_data)
    address_data = {
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip_code': request.form['zip_code'],
        'project_id': project_id.id
    }
    Address.save_with_project(address_data)
    contact_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'project_id': project_id.id,
        'title_id': request.form['title'],
        'customer_id': request.form['customer']
    }
    Contact.save_with_project(contact_data)
    return redirect('/dashboard')

@app.route('/projects/delete/<int:id>')
def delete_project(id):
    if "user_id" not in session:
        return redirect('/login') 
    data = {
        'project_id': id,
        'id': id
    }
    Contact.null_project_id(data)
    Address.delete_proj_address(data)
    Project.delete(data)
    return redirect('/dashboard')


