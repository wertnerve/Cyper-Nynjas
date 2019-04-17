import socket                   # Import socket module
import sys
from PIL import Image
from io import StringIO, BytesIO
import tkinter
from tkinter import filedialog

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
port = 9999                    # Reserve a port for your service.

s.connect((host, port))
'''
filetosend = filedialog.askopenfilename()
with open(filetosend, "rb") as f:
    data = f.read()
    bytes = bytearray(data)
    s.send(bytes)
    print('Successfully get the file')
    '''
s.send(bytes("hi", 'utf-8'))
msg, ancdata, flags, addr = s.recvmsg(4096)
print(msg)

print('connection closed')
