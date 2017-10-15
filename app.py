from flask import Flask, render_template
#from client import Client

app = Flask(__name__)

#data = Client()

@app.route('/test')
def name():

    variables = list()

    variables.append("Ola marajulha")
    variables.append("como vai")
    variables.append("a matilda")

    return render_template('index.html', variable=['46', '47', '48', '49'])

@app.route('/')
def index():
    #data.connect()
    return render_template('index.html', variable=variable)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
