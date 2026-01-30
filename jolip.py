from flask import Flask

jolipApp = Flask(__name__)

@jolipApp.route ('/')
def home():
    return '<h1>pimis</h1>'

if __name__=='__main__':
    jolipApp.run(port=5000, debug=True)

