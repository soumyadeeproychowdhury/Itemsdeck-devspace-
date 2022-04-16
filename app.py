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
    high_val=0
    low_val=0
    average_val=0
    cp_average=0
    ideal_1=0
    ideal_2=0
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

    else:
        otp = 'product found below are the details'
        l=list()
        sum_s = 0
        sum_c=0
        for r in rec:
            l.append(r[3])
            sum_s+=r[3]
            sum_c+=r[2]
        high_val=max(l)
        low_val=min(l)
        average_val=(sum_s/ctr)
        cp_average=(sum_c/ctr)
        ideal_1=(average_val-(average_val*0.05))
        ideal_2=(average_val+(average_val*0.06))
        
    return render_template("ItemDeck.html", output_variable = otp, hv=high_val, lv=low_val, av=average_val, ca=cp_average, i1=ideal_1, i2=ideal_2)
