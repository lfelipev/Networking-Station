from flask import Flask, render_template
from client import Client

app = Flask(__name__)

data = Client()

@app.route('/test')
def name():

    variables = list()

    variables.append("v1")
    variables.append("v2")
    variables.append("v3")

    return render_template('index.html', variable=variables)

@app.route('/')
def index():
    data.connect()
    return render_template('index.html', variable=variable)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')