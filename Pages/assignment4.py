from flask import Flask, Blueprint, render_template, request, jsonify

from db.db_manager import interact_db

assignment4 = Blueprint('assignment4', __name__)


@assignment4.route('/assignment4')
def assignment4_page():
    return render_template('assignment4.html')


@assignment4.route('/assignment4/insertion', methods=['GET', 'POST'])
def assignment4_insertion():
    if request.method == 'POST':
        user_id = request.form['insertion-id']
        user_name = request.form['insertion-name']
        user_email = request.form['insertion-email']

        db_query = "INSERT INTO users(id, name, email) VALUES ('%s', '%s', '%s')" % (user_id, user_name, user_email)
        interact_db(query=db_query, query_type='commit')

    return render_template('assignment4.html')


@assignment4.route('/assignment4/delete', methods=['GET', 'POST'])
def assignment4_delete():
    delete_id = request.form['delete-id']
    query = "DELETE FROM users WHERE id='%s';" % delete_id
    interact_db(query=query, query_type='commit')
    return render_template('assignment4.html')


@assignment4.route('/assignment4/update', methods=['GET', 'POST'])
def assignment4_update():
    user_id = request.form['update-id']
    user_name = request.form['update-name']
    user_email = request.form['update-email']
    query = "UPDATE users SET name='%s', email='%s' WHERE id='%s'" % (user_name, user_email, user_id)
    interact_db(query=query, query_type='commit')

    return render_template('assignment4.html')


@assignment4.route('/assignment4/users', methods=['GET', 'POST'])
def assignment4_show_all():
    query = 'select * from users'
    db_users = interact_db(query=query, query_type='fetch')

    return jsonify(db_users)

