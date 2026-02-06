from flask import Flask, render_template
import json

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)