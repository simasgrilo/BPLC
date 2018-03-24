import socket
import sys

message = \
"""
from flask import Flask 
import atexit 
import cf_deployment_tracker 
import os 
import json 
import fact 

# Emit Bluemix deployment event 
cf_deployment_tracker.track() 
app = Flask(__name__) 
client = None

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return str(fact.fact(10))

@atexit.register
def shutdown():
    if client:
       client.disconnect()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
"""

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Send data
print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)
sock.close()
    