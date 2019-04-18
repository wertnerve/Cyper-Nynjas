import socket                   # Import socket module
import sys
from PIL import Image
from io import StringIO, BytesIO
from tkinter import *
from tkinter import filedialog

#Connect to a server, currently hosted on localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
port = 9999                    # Reserve a port for your service.
s.connect((host, port))

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
    global filetosend
    f = filedialog.askopenfilename()
    filetosend = f

btn = Button(window, text="Choose a File", command = clicked)
btn.grid(column=1, row=0)
btn2 = Button(window, text="Click to Close", command = window.destroy)
btn2.grid(column = 1, row = 1)
window.mainloop()

#Open file as binary data and send it to the server
with open(filetosend, "rb") as f:
    data = f.read()
    s.send(data)
    print('Successfully get the file')

#If a message is sent by the server, recieve the tuple; 'msg' is the var of interest here
msg, ancdata, flags, addr = s.recvmsg(4096)
print(msg)

print('connection closed')
