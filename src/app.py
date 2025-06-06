# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from datetime import datetime
from socket import socket
from flask import Flask, jsonify

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/details')
# ‘/’ URL is bound with hello_world() function.


def details():
    return jsonify({
        'time' : datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
#        'hostname' : socket.gethostbyaddr(socket.gethostname())[0],
         'message' : 'You are doing great, likith :) :) :)'
    })

@app.route('/api/v1/health')
def heatlh():
    return jsonify({
        
        'status' : 'up'
    }), 200



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")

