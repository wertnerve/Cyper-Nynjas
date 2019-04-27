#NEED TO ADD OPTION TO GUI TO CHOOSE WHAT FILE THE IMAGE IS READ INTO

import socket                   # Import socket module
import sys
from PIL import Image
from io import StringIO, BytesIO
from tkinter import *
from tkinter import filedialog

def sendFile(filetosend):
    with open(filetosend, "rb") as myfile:
        data = myfile.read()
        s.send(data)
        print('Successfully send the file')
        clientfile = open('encrypted-image.jpg', 'wb')
    while True:
        try:
            msg, ancdata, flags, addr = s.recvmsg(999999999)
            clientfile.write(msg)
            # conn.send(msg)
        except:
            print('no more bytes')


#Connect to a server, currently hosted on localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
port = 60000                   # Reserve a port for your service.
s.connect(('66.195.11.250', port))

#Create basic GUI for easy file input
window = Tk()
window.title("Send a File")
window.geometry('350x200')
lbl = Label(window, text="File Upload")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

#Function that allows user to select a file through Tkinter's GUI
def clicked():
    f = filedialog.askopenfilename()
    sendFile(f)

btn = Button(window, text="Choose a File", command = clicked)
btn.grid(column=1, row=0)
btn2 = Button(window, text="Click to Close", command = window.destroy)
btn2.grid(column = 1, row = 1)
window.mainloop()


print('connection closed')
