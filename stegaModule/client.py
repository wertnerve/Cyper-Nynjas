#NEED TO ADD OPTION TO GUI TO CHOOSE WHAT FILE THE IMAGE IS READ INTO
#This is the working program NOT client.py
import socket
from tkinter import *
from tkinter import filedialog, messagebox

def sendFile(filename):
    with open(filename, "rb") as myfile:
        print('file opened')
        data = myfile.read()
        print('data read')
    s.send(data)
    print('Successfully send the file')

def recieveFile():
    messagebox.showinfo("", "Please create a file in which to store the recieved image.")
    myfile = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                 filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    window.update()
    clientfile = open(myfile, 'wb')
    while True:
        try:
            msg, ancdata, flags, addr = s.recvmsg(999999999)
            print('received data')
            clientfile.write(msg)
        except:
            clientfile.close()
            print('no more bytes')

#Connect to a server, currently hosted on localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostbyname('localhost')     # Get local machine name
port = 60000                   # Reserve a port for your service.
s.connect(('192.168.43.103', port))

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
    messagebox.showinfo("","File sent!")
    window.update()

btn = Button(window, text="Send File", command = clicked)
btn.grid(column=1, row=0)
btn2 = Button(window, text="Recieve File", command = recieveFile)
btn2.grid(column = 1, row = 1)
window.mainloop()