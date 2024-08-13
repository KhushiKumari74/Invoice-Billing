from flask import Flask, render_template, redirect
import pandas as pd
from function import conn, delete


app = Flask(__name__)

@app.route("/clients")
def clients():
    with conn.cursor() as cur:
        sql="select * from clients"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
    return render_template("client.html", data=data)

@app.route("/client/<param>/<id>")
def client_ops(param, id):
    if param=="delete":
        delete("clients", "client_id", id)
        return redirect("/clients")
    if param=="add":
        return render_template("client-form.html")

@app.route("/inoiceitems/<param>/<id>")
def invoiceitem(param, id):
    if param=="delete":
        delete("invoiceitems", "item_id", id)
        return redirect("/invoiceitems")
     
    if param=="add":
       return render_temp("invoiceitemsform.html")

@app.route("/invoiceitems")
def invoiceitems():
    with conn.cursor() as cur:
        sql="select * from invoiceitems"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
    return render_template("invoiceitems.html",data=data)

@app.route("/invoices/<param>/<id>")
def invoiceops(param, id):
    if param=="delete":
        delete("invoices", "invoice_id", id)
        return redirect("/invoices")
    if param=="add":
       return render_temp("invoicesform.html")



@app.route("/invoices")
def invoice():
    with conn.cursor() as cur:
        sql="select * from invoices"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
    return render_template("invoices.html",data=data)

@app.route("/payments/<param>/<id>")
def payments_ops(param, id):
    if param=="delete":
        delete("payments", "payment_id", id)
        return redirect("/payments")
    if param=="add":
       return render_temp("paymentsform.html")


@app.route("/payments")
def invoices():
    with conn.cursor() as cur:
        sql="select*from payments"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
    return render_template("payments.html",data=data)

@app.route("/projects/<param>/<id>")
def project_ops(param, id):
    if param=="delete":
        delete("projects", "item_id", id)
        return redirect("/projects")
    if param=="add":
       return render_temp("projectsform.html")



@app.route("/projects")
def projects():
    with conn.cursor() as cur:
        sql="select * from projects"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
    return render_template("projects.html",data=data)           

if __name__=="__main__":
    app.run(debug=True)