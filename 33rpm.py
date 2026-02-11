from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import hashlib
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

app.secret_key = "super_secret_key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "mysql"   
app.config["MYSQL_DB"] = "rpm33"
 

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/biblioteca")
def biblioteca():
    with open("library.json", encoding="utf-8") as f:
        albums = json.load(f)
    return render_template("biblioteca.html", albums=albums)

@app.route("/reproductor")
def reproductor():
    return render_template("reproductor.html")

@app.route("/ventas")
def ventas():
    return render_template("ventas.html")

@app.route("/auth")
def auth():
    return render_template("auth.html")

if __name__ == "__main__":
    app.run(debug=True)

