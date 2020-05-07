from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)

# Mysql connection

app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] ='root'
app.config['MYSQL_DATABASE_PASSWORD'] =''
app.config['MYSQL_DATABASE_DB'] ='contacs'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur = mysql.get_db().cursor()
        cur.execute('INSERT INTO contacts(fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.get_db().commit()
        flash('Contact Added successfully')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT* FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.get_db().cursor()
        cur.execute("UPDATE contacts SET fullname = %s, email = %s, phone = %s WHERE id = %s", (fullname, email, phone, id))
        mysql.get_db().commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.get_db().cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.get_db().commit()
    flash('Contact Removed Succesfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)