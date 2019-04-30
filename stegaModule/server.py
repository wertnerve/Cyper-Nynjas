import socket                   # Import socket module
import time

port = 60000                 # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
s.bind(('', port))            # Bind to the port
print ('Server listening....')
s.listen(2)                     # Now wait for client connection.
conn, addr = s.accept()
print('Got connection from', addr)

def handleConn():
    #time.sleep(5)
    myfile = open('encrypted-image.jpg','wb')
    while True:
        try:
            msg, ancdata, flags, addr = conn.recvmsg(999999999)
            print('Got message!')
            conn.send(msg)
            print('Listening for messages')
        except:
            print('no more bytes')
            return False
while True:
    handleConn()


