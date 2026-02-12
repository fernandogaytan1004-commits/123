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

@app.route("/register", methods=["POST"])
def register():

    nombre = request.form["nombre"]
    correo = request.form["correo"]
    password = request.form["password"]

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nombre, correo, password) VALUES (%s, %s, %s)",
        (nombre, correo, hashed_password)
    )
    mysql.connection.commit()

    return redirect("/auth")

@app.route("/login", methods=["POST"])
def login():

    correo = request.form["correo"]
    password = request.form["password"]

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM usuarios WHERE correo = %s AND password = %s",
        (correo, hashed_password)
    )

    user = cursor.fetchone()

    if user:
        session["loggedin"] = True
        session["id"] = user["id"]
        session["nombre"] = user["nombre"]
        return redirect("/")
    else:
        return "Correo o contraseña incorrectos"
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

