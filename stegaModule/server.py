import socket                   # Import socket module
from io import StringIO
from PIL import Image
import tkinter
from tkinter import filedialog
from io import BytesIO

port = 9999                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(1)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    msg, ancdata, flags, addr = s.recvmsg(4096)
    #im = Image.open(BytesIO(data))
    conn.send(msg)

print("[+] Download complete!")

