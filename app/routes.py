# from datetime import date, datetime
# from view import create
from flask import render_template, request, redirect, url_for, flash, jsonify, json, abort
# from flask_sqlalchemy import SQLAlchemy
from app import app
from app.models import ContactBook
from flask_paginate import Pagination, get_page_parameter
from app import db


@app.route('/', methods=['GET'])
def index():
    # adding search query
    q = request.args.get('q')

    if q:
        cb = ContactBook.query.filter(ContactBook.first_name.contains(q) | ContactBook.last_name.contains(q) |
                                      ContactBook.email.contains(q) | ContactBook.phone_number.contains(q))

    elif q == '':
        cb = ContactBook.query.all()
    else:
        cb = ContactBook.query.all()

    return render_template('index.html', cb=cb)

# index, search, and pagination
# @app.route('/', methods=['GET'])
# def index():
#     # adding search query
#     q = request.args.get('q')
#
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 5, type=int)
#
#     if q:
#         cb = ContactBook.query.filter(ContactBook.first_name.contains(q) | ContactBook.last_name.contains(q) |
#                                       ContactBook.email.contains(q) | ContactBook.phone_number.contains(q)).paginate(
#             page=page, per_page=per_page, error_out=False)
#
#     elif q == '':
#         cb = ContactBook.query.paginate(page=page, per_page=per_page, error_out=False)
#     else:
#         cb = ContactBook.query.paginate(page=page, per_page=per_page, error_out=False)
#
#     return render_template('index.html', cb=cb)


@app.route('/add', methods=['POST'])
def add():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    # date_created = request.form['date_created']

    cb = ContactBook(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)

    db.session.add(cb)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/view', methods=['GET', 'POST'])
def viewaddress():
    # cb = ContactBook.query.filter_by(id=int(id)).first()
    cb = ContactBook.query.all()
    # if request.method == 'POST':
    #     return redirect(url_for('index.html'))

    return render_template('index.html', cb=cb)


# @app.route('/delete/<int:id>', methods=['POST'])
# def delete(id):
#     cb = ContactBook.query.get(id)
#
#     db.session.delete(cb)
#     db.session.commit()
#
#     return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cb = ContactBook.query.get(id)
    if cb is None:
        flash('Contact not found')
        return redirect(url_for('index'))

    db.session.delete(cb)
    db.session.commit()

    return redirect(url_for('index'))

# @app.route('/update/<id>', methods=["GET", "POST"])
# def update(id):
#     cb = ContactBook.query.filter_by(id=int(id)).first()
#     if request.method == 'GET':
#         # Return the update modal with the contact data
#         return render_template('update_modal.html', cb=cb)
#     elif request.method == 'POST':
#         # Update the contact data in the database
#         cb.first_name = request.form['first_name']
#         cb.last_name = request.form['last_name']
#         cb.phone_number = request.form['phone_number']
#         cb.email = request.form['email']
#         db.session.commit()
#         # Redirect to the index route
#         return redirect(url_for('index'))

#
# @app.route('/update/<id>', methods=["GET", "POST"])
# def update(id):
#     # Retrieve the contact data
#     cb = ContactBook.query.filter_by(id=int(id)).first()
#
#     if request.method == 'POST':
#         # Update the contact data
#         data = request.get_json()
#         cb.first_name = data['first_name']
#         cb.last_name = data['last_name']
#         cb.phone_number = data['phone_number']
#         cb.email = data['email']
#         db.session.commit()
#         return jsonify({'success': True}), 200
#
#     # Return the contact data as a JSON response
#     return jsonify({'first_name': cb.first_name, 'last_name': cb.last_name, 'phone_number': cb.phone_number,
#                     'email': cb.email}), 20

#
# @app.route('/update/<id>', methods=["GET", "POST"])
# def update(id):
#     cb = ContactBook.query.get(id)
#
#     if request.method == 'GET':
#         return render_template('update.html', cb=cb)
#     elif request.method == 'POST':
#         data = request.get_json()
#
#         id = request.form['id']
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         phone_number = request.form['phone_number']
#         email = request.form['email']
#
#         cb = ContactBook(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
#
#         db.session.add(cb)
#         db.session.commit()
#         return jsonify({'success': True}), 200
#         flash('The contact has been updated!')
#         return redirect(url_for('index'))

# @app.route('/update/<id>', methods=["GET", "POST"])
# def update(id):
#     cb = ContactBook.query.get(id)
#     if request.method == 'POST':
#         # Update the contact in the database
#         cb.first_name = request.form['first_name']
#         cb.last_name = request.form['last_name']
#         cb.email = request.form['email']
#         cb.phone_number = request.form['phone_number']
#         db.session.commit()
#         flash('The contact has been updated!')
#         return redirect(url_for('index'))
#     # Return the contact data as a JSON response to the JavaScript function
#     return jsonify({
#         'id': cb.id,
#         'first_name': cb.first_name,
#         'last_name': cb.last_name,
#         'email': cb.email,
#         'phone_number': cb.phone_number
#     })


# @app.route('/update/<id>', methods=["GET", "POST"])
# def update(id):
#     # Retrieve the contact data from the database
#     cb = ContactBook.query.get(id)
#
#     # Handle the GET request
#     if request.method == "GET":
#         # Return the contact data as a JSON object
#         return jsonify(cb.to_dict())
#
#     # Handle the POST request
#     if request.method == "POST":
#         # Update the contact in the database
#         cb.first_name = request.form['first_name']
#         cb.last_name = request.form['last_name']
#         cb.phone_number = request.form['phone_number']
#         cb.email = request.form['email']
#         db.session.commit()
#
#         # Return a JSON object indicating that the update was successful
#         return jsonify({'success': True})


# @app.route('/update/<int:id>', methods=['POST'])
# def update_contact(id):
#     # Get the updated contact data from the request
#     first_name = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     email = request.form.get('email')
#     phone_number = request.form.get('phone_number')
#
#     # Update the contact in the database
#     cb = ContactBook.query.get(id)
#     cb.first_name = first_name
#     cb.last_name = last_name
#     cb.email = email
#     cb.phone_number = phone_number
#     db.session.commit()
#
#     # Redirect to the home page
#     return redirect(url_for('index'))


# @app.route('/update/<int:id>')
# def update(id):
#     cb = ContactBook.query.get(id)
#     cb_json = json.dumps(cb.__dict__)
#     return render_template('index.html', cb=cb_json)


# @app.route('/update/<int:id>')
# def update(id):
#     cb = ContactBook.query.get(id)
#     return render_template('update.html', cb=cb)

#
# @app.route('/update/<id>', methods=['POST'])
# def update(id):
#     cb = ContactBook.query.filter_by(id=id).first()
#
#     cb.first_name = request.form['first_name']
#     cb.last_name = request.form['last_name']
#     cb.phone_number = request.form['phone_number']
#
#     db.session.commit()
#
#     flash('Contact updated successfully')
#     return redirect(url_for('index'))


# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     cb = ContactBook.query.get(id)
#     if request.method == 'POST':
#         cb.first_name = request.form['first_name']
#         cb.last_name = request.form['last_name']
#         cb.phone_number = request.form['phone_number']
#         cb.email = request.form['email']
#         db.session.commit()
#         flash('Contact updated successfully!')
#         return redirect(url_for('index'))
#     return render_template('update.html', cb=cb)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # Check if the contact exists before trying to update it
    cb = ContactBook.query.get(id)
    if cb is None:
        flash('Contact does not exist')
        return redirect(url_for('index'))

    if request.method == 'POST':
        cb.first_name = request.form['first_name']
        cb.last_name = request.form['last_name']
        cb.phone_number = request.form['phone_number']
        cb.email = request.form['email']
        db.session.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('index'))
    return render_template('update.html', cb=cb)


@app.route('/search')
def search():
    search_query = request.args.get('q')
    search_results = db.query(search_query)
    return jsonify(search_results)
