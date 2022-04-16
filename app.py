from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from numpy import product

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Aayu$0393'
app.config['MYSQL_DATABASE_DB'] = 'itemsdeck'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

@app.route("/")
def ItemDeck():
    otp = "none"
    temp = request.args.get("product")
    cursor.execute("SELECT * from mytable WHERE name LIKE '{name}'".format(name=temp))
    rec=cursor.fetchall()
    ctr = cursor.rowcount
    if ctr <=0:
        otp = 'product not found in database'
        b = request.args.get('brand')
        cost_price=request.args.get('cp')
        selling_price=request.args.get('sp')
    
    return render_template("ItemDeck.html", output_variable = otp)