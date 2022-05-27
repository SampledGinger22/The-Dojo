from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.customer import Customer
from flask_app.models.project import Project
from flask_app.models.contact import Contact
from flask_app.models.address import Address
from flask_app.models.title import Title

@app.route('/contacts/dash')
def contacts_dash():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id']
    }
    context = {
        'contacts': Contact.get_all(data),
        'projects': Project.get_all(data),
        'customers': Customer.get_all(data)
    }
    return render_template('dash_contacts.html', **context)

@app.route('/contacts/projects/<int:id>/<int:customer_id>/new')
def new_proj_contact(id, customer_id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'project_id': id,
        'customer_id': customer_id
    }
    context = {
        'data': data,
        'titles': Title.get_all()
    }
    return render_template('new_project_contact.html', **context)

@app.route('/contacts/projects/<int:id>/<int:customer_id>/new/commit', methods=['POST'])
def new_proj_contact_commit(id, customer_id):
    data = {
        'customer_id': customer_id,
        'project_id': id,
        **request.form
    }
    Contact.save_proj_cont(data)
    return redirect('/dashboard')

@app.route('/contacts/customers/<int:id>/new')
def new_cust_contact(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'customer_id': id,
    }
    context = {
        'data': data,
        'titles': Title.get_all()
    }
    return render_template('new_cust_contact.html', **context)

@app.route('/contacts/projects/<int:id>/new/commit', methods=['POST'])
def new_cust_contact_commit(id):
    data = {
        'customer_id': id,
        **request.form
    }
    Contact.save_cust_cont(data)
    return redirect('/dashboard')

@app.route('/contacts/view/<int:id>')
def view_contact(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id':id
    }
    context = {
        'contact' : Contact.get_one(data),
        'titles': Title.get_all()
    }
    return render_template('view_contact.html', **context)

@app.route('/contacts/view/<int:id>/primary')
def view_primary_contact(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id':id
    }
    context = {
        'contact' : Contact.get_one(data),
        'titles': Title.get_all()
    }
    return render_template('view_primary_cont.html', **context)

@app.route('/contacts/edit/<int:id>/commit', methods=['POST'])
def contacts_update_commit(id):
    data = {
        'id': id,
        **request.form
    }
    Contact.update(data)
    return redirect('/dashboard')

@app.route('/contacts/delete/<int:id>')
def delete_contact(id):
    data = {
        'id': id,
    }
    Contact.delete(data)
    return redirect(request.referrer)
