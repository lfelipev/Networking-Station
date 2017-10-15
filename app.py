from flask import Flask, render_template
#from client import Client

app = Flask(__name__)

#data = Client()

@app.route('/test')
def name():
    return render_template('index.html', variables=['46', '47', '48', '49'])

@app.route('/')
def index():
    #data.connect()
    return render_template('index.html', variable=variable)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
