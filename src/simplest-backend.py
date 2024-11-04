from flask import Flask
import socket

app = Flask(__name__)

def get_backend_signature():
    return '\n<i>You have been served by: ' + socket.gethostname() + '<i>\n'

@app.route('/')
def home():
    return '<html><head><title>KIV/DCE - Simplest backend</title></head>' + \
           '<body><h2>Simplest backend</h2>' + \
           '<p>Welcome!</p>' + \
           get_backend_signature() + '</body></html>\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
