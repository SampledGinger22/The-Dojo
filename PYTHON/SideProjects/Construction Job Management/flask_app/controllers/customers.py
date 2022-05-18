from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.customer import Customer
from flask_app.models.project import Project
from flask_app.models.contact import Contact
from flask_app.models.address import Address

@app.route('/customers/dash')
def customer_dash():
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'user_id': session['user_id']
    }
    Customer.get_all(data)
    return render_template('dash_customers.html')

@app.route('/customers/new')
def new_customer():
    if "user_id" not in session:
        return redirect('/login')
    return render_template('new_customer.html')

@app.route('/customers/new/commit', methods=('POST'))
def new_customer_commit():
    data = {
        **request.form
    }
    Customer.save(data)
    return redirect('/customers/dash')

@app.route('/customers/<int:id>')
def view_customer(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id':id
    }
    context = {
        'customer' : Customer.get_one(data),
        'address' : Address.get_one_by_customer(data),
        'contact' : Contact.get_by_customer(data),
        'project' : Project.get_by_customer(data)
    }
    return render_template('view_customer.html', **context)

@app.route('/customers/edit/<int:id>')
def edit_customer(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id': id
    }
    Customer.get_one(data)
    return render_template('edit_customer.html')

@app.route('/customers/edit/commit', methods=('POST'))
def customer_edit_commit():
    data = {
        **request.form
    }
    Customer.save(data)
    return redirect('/customers/<int:id>')