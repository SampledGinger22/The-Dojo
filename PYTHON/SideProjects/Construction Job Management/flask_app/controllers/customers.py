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

@app.route('/customers/new/commit', methods=['POST'])
def new_customer_commit():
    disp_data = {
        'display_name': request.form['display_name']
    }
    if not Customer.validate(disp_data):
        return redirect('/customers/new')
    cust_data = {
        'display_name': request.form['display_name'],
        'notes': request.form['cust_notes'],
        'user_id': session['user_id']
    }
    Customer.save(cust_data)
    cust_id = Customer.get_by_disp(cust_data)
    address_data = {
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip_code': request.form['zip_code'],
        'customer_id': cust_id.id
    }
    Address.save_with_customer(address_data)
    contact_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'phone': request.form['phone'],
        'email': request.form['email'],
        'customer_id': cust_id.id,
        'title_id': 1
    }
    Contact.save_with_customer(contact_data)
    return redirect('/dashboard')

@app.route('/customers/view/<int:id>')
def view_customer(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'customer_id': id,
    }
    context = {
        'customer' : Customer.get_one(data),
        'primaries': Contact.get_primary(data),
        'contacts': Contact.get_by_customer(data),
        'projects': Project.get_by_customer(data),
        'address': Address.get_one_by_customer(data)
    }
    return render_template('view_customer.html', **context)

@app.route('/customers/edit/<int:id>/commit', methods=["POST"])
def customer_edit_commit(id):
    disp_data = {
        'display_name': request.form['display_name']
    }
    if not Customer.validate_update(disp_data):
        return redirect('/dashboard')
    data = {
        'id': id,
        **request.form
    }
    Customer.update(data)
    address_data = {
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip_code': request.form['zip_code'],
        'customer_id': id
    }
    Address.update_with_cust(address_data)
    return redirect('/dashboard')