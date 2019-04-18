import socket                   # Import socket module
from io import StringIO
from PIL import Image
from io import BytesIO

#Create a server based out of port 9999, hosted on localhost
port = 9999                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(3)                     # Now wait for client connection.

print ('Server listening....')

#Continually loop to accept the clients, max of 3
while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    #If message is sent to the server, receive the tuple
    msg, ancdata, flags, addr = s.recvmsg(4096)
    #Do something with the binary data (still figuring it out)
    #im = Image.open(BytesIO(data))
    conn.send(msg)

print("[+] Download complete!")

