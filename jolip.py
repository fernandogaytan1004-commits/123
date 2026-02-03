from flask import Flask, render_template, url_for

jolipApp = Flask(__name__)

@jolipApp.route ('/')
def home():
    return render_template

if __name__=='__main__':
    jolipApp.run(port=5000, debug=True)

