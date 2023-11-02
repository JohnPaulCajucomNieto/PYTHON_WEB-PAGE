from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

myconn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='customer'
)
mycursor = myconn.cursor()


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM customerorders")
    customer_data = mycursor.fetchall()
    return render_template("index.html", c=customer_data)


@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/table', methods=['GET'])
def table():
    mycursor.execute("SELECT * FROM customerorders")
    customer = mycursor.fetchall()
    return render_template('table.html', c=customer)

@app.route('/update')
def update():
    return render_template("update.html")

@app.route('/form', methods=['POST', 'GET'])
def add_order():
    if request.method == 'POST':
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        FullAddress = request.form['FullAddress']
        EmailAddress = request.form['EmailAddress']
        PhoneNumber = request.form['PhoneNumber']
        Instrument = request.form['Instrument']
        Qty = int(request.form['Qty'])
        Brand = request.form['Brand']


        sql = """
            INSERT INTO customerorders (Firstname, Lastname, FullAddress, EmailAddress, PhoneNumber, Instrument, Qty, Brand)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (Firstname, Lastname, FullAddress, EmailAddress, PhoneNumber, Instrument, Qty, Brand)
        mycursor.execute(sql, data)
        myconn.commit()

    return redirect('/table')

@app.route('/update_form/<int:id>', methods=['GET'])
def update_form(id):
    mycursor = myconn.cursor()
    sql = "SELECT * FROM customerorders WHERE id=%s"
    data = (id,)
    mycursor.execute(sql, data)
    myresult = mycursor.fetchall()

    if myresult:
        return render_template('update.html', myresult=myresult)

@app.route('/update', methods=['POST', 'GET'])
def update_order():
    if request.method == 'POST':
        id = request.form['id']
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        FullAddress = request.form['FullAddress']
        EmailAddress = request.form['EmailAddress']
        PhoneNumber = request.form['PhoneNumber']
        Instrument = request.form['Instrument']
        Qty = int(request.form['Qty'])
        Brand = request.form['Brand']

        mycursor = myconn.cursor()
        sql = "UPDATE customerorders SET Firstname = %s, Lastname = %s, FullAddress = %s, EmailAddress = %s, PhoneNumber = %s, Instrument = %s, Qty = %s, Brand = %s WHERE id = %s"
        data = (Firstname, Lastname, FullAddress, EmailAddress, PhoneNumber, Instrument, Qty, Brand, id)
        mycursor.execute(sql, data)
        myconn.commit()

        return redirect('/table')

@app.route('/delete_order/<id>', methods=['GET'])
def delete_order(id):
    mycursor = myconn.cursor()
    sql = "DELETE FROM customerorders WHERE id = %s"
    data = (id,)
    mycursor.execute(sql, (data))
    myconn.commit()
    return redirect('/table')

if __name__ == '__main__':
    app.run(debug=True)
