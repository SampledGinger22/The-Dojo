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
        'contacts': Contact.get_all(data)
    }
    return render_template('dash_contacts.html', **context)

@app.route('/contacts/new')
def new_contact():
    if "user_id" not in session:
        return redirect('/login')
    titles = Title.get_all
    return render_template('new_contact.html', title = titles)

@app.route('/contacts/new/commit', methods=['POST'])
def new_contact_commit():
    data = {
        **request.form
    }
    Contact.save(data)
    return redirect('/contacts/dash')

@app.route('/contacts/view/<int:id>')
def view_contact(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id':id
    }
    context = {
        'contact' : Contact.get_one(data)
    }
    return render_template('view_contact.html', **context)

@app.route('/contacts/edit/<int:id>')
def edit_contacts(id):
    if "user_id" not in session:
        return redirect('/login')
    data = {
        'id': id
    }
    Contact.get_one(data)
    return render_template('edit_contact.html')

@app.route('/contacts/edit/commit', methods=['POST'])
def contacts_edit_commit():
    data = {
        **request.form
    }
    Contact.save(data)
    return redirect('/contacts/<int:id>')

@app.route('/contacts/delete/<int:id>')
def delete_contact(id):
    data = {
        'id': id,
    }
    Contact.delete(id)
    return redirect('/customers/<int:customer_id>')
