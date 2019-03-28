from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import os

def change_lay(l1, l2, l3, e1, e2, e3, r4, numb="3"):
    if numb == 1:
        l1.grid(row=1)
        e1.grid(row=1, column=1, columnspan=2)
        l3.grid(row=2)
        e3.grid(row=2,column=1, columnspan=2)
        l2.grid_forget()
        e2.grid_forget()

        r4.configure(text="Encrypt Message", command=lambda :runSt(L1, L2, L3, E1, E2, E3, R4, 1))
    elif numb == 2:
        l2.grid(row=1)
        e2.grid(row=1, column=1, columnspan=2)
        l3.grid_forget()
        e3.grid_forget()
        l1.grid_forget()
        e1.grid_forget()

        r4.configure(text="Decrypt Message", command=lambda :runSt(L1, L2, L3, E1, E2, E3, R4, 2))
    else:
        print("erorr")
    return


def selectF(root):
    global filename
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Image file",filetypes = (("jpeg files","*.png"),("all files","*.*")))


def runSt(l1, l2, l3, e1, e2, e3, r4, numb="3"):
    if numb == 1:
        print(e1.get())
        print(e3.get())
        print(filename)
    elif numb == 2:
        print(e2.get())
        print(filename)
    else:
        print("Error")
        
    

filename="No File Selected"
root = Tk()
root.title("Stegasaurus")
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'Cyper-Nynjas-master\stegaModule\steg.ico')
# os.path.normpath(filename)
# root.iconbitmap(r'E:\Cyper-Nynjas-master\stegaModule\steg.ico')

L2 = Label(root, text="Decryption Key:")
E2 = Entry(root, bd=5)

L1 = Label(root, text="Encryption Key:")
E1 = Entry(root, bd=5)

R1 = Button(root, text="Encrypt", command=lambda :change_lay(L1, L2, L3, E1, E2, E3, R4, 1)).grid(row=0, column=0)


R2 = Button(root, text="Decrypt", command=lambda :change_lay(L1, L2, L3, E1, E2, E3, R4, 2)).grid(row=0, column=2)


L3 = Label(root,text="Text to be Encrypted:")
E3 = Entry(root,bd=4)

R3 = Button(root, text="Select Image File", command=lambda :selectF(root))


R4 = Button(root, text="Encrypt Message", command=lambda :runSt(L1, L2, L3, E1, E2, E3, R4, 1))

L1.grid(row=1)
E1.grid(row=1, column=1, columnspan=2)
L3.grid(row=2)
E3.grid(row=2,column=1, columnspan=2)

R3.grid(row=3,column=0, columnspan=3)
R4.grid(row=4,column=0, columnspan=3)

root.mainloop()

            
