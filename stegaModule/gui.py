from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import os
import characterEncrypt
import characterDecrypt
import globalVariables

#testing commit
def change_lay(l1, l2, l3, e1, e2, e3, r4, numb="3"):
    if numb == 1:
        l1.grid(row=1)
        e1.grid(row=1, column=1, columnspan=2)
        l3.grid(row=2)
        e3.grid(row=2,column=1, columnspan=2)
        l2.grid_forget()
        e2.grid_forget()

        r4.configure(text="Encrypt Message", font = ('Arial',12), command=lambda: runSt(L1, L2, L3, E1, E2, E3, R4, 1))
    elif numb == 2:
        l2.grid(row=1, rowspan=1)
        e2.grid(row=1, column=1, columnspan=2, rowspan=1)
        l3.grid_forget()
        e3.grid_forget()
        l1.grid_forget()
        e1.grid_forget()

        r4.configure(text="Decrypt Message", font = ('Arial',12), command=lambda: runSt(L1, L2, L3, E1, E2, E3, R4, 2))
    else:
        print("erorr")
    return


def selectF(root):
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    

def runSt(l1, l2, l3, e1, e2, e3, r4, numb="3"):
    if checkErrors(l1, l2, l3, e1, e2, e3, r4, numb):
        if numb == 1:
            #e1: password
            #e2: plaintext
            print(e1.get())
            print(e3.get())
            print(filename)

            characterEncrypt.encrypt(filename, e3.get(),str(e1.get()))

        elif numb == 2:
            print(e2.get())
            #this wont work if user just decrypts without encyrpting first
            print(filename)
            #as work around for char length, use len(e3.get())
            characterDecrypt.decrypt(filename, str(e1.get()))
        else:
            print("Error")
        
def openHelp():
    help = Tk()
    help.title = "Help Menu"
    HL = Label(help, text="Help Info will Go Here")
    HL.grid(row=0)

def openFAQ():
    FAQ = Tk()
    FAQ.title = "Help Menu"
    FL = Label(FAQ, text="FAQ Info will Go Here")
    FL.grid(row=0)
def checkErrors(l1, l2, l3, e1, e2, e3, r4, numb):
    if(str(e1.get()).isupper() or str(e1.get()).islower()) or str(e1.get()) == "" or str(e2.get()) == "" or str(e3.get() == "") or filename == "No File Selected":
        x=False
        
        if(str(e1.get()).isupper() or str(e1.get()).islower()):
            x=True
            message="Key Must be Numbers Only"
        if(numb == 1 and str(e1.get()) == ""):
            x=True
            message = "Encryption Key Must Not Be Empty"
        if(numb == 2 and str(e2.get()) == ""):
            x=True
            message = "Decrpytion Key Must Not Be Empty"
        if(numb == 1 and str(e3.get()) == ""):
            x=True
            message = "Text Field Must Not Be Empty"
        if(filename == "No File Selected"):
            x=True
            message = "File Must Be Selected"
        if(x):
            erwin = Tk()
            erwin.title = "Error"
            EWL = Label(erwin, text=message, font = ('Arial',12))
            EWL.grid(row=0)
            return False
        else:
            return True
    else:
        return True


filename = "No File Selected"
root = Tk()
root.title("Stegasaurus")


dir_path = os.path.dirname(os.path.realpath(__file__))
root.iconbitmap(r''+dir_path+'\steg.ico')

# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Close Application", command=lambda: root.destroy())
menubar.add_command(label="Open Help", command=lambda: openHelp())
menubar.add_command(label="FAQ", command=lambda: openFAQ())
# display the menu
root.config(menu=menubar)
L2 = Label(root, text="Decryption Key:", font = ('Arial',12))
E2 = Entry(root, bd=1)

L1 = Label(root, text="Encryption Key:", font = ('Arial',12))
E1 = Entry(root, bd=1)

R1 = Button(root, text="Encrypt",  font = ('Arial',12), command=lambda :change_lay(L1, L2, L3, E1, E2, E3, R4, 1)).grid(row=0, column=0)


R2 = Button(root, text="Decrypt", font = ('Arial',12) ,command=lambda: change_lay(L1, L2, L3, E1, E2, E3, R4, 2)).grid(row=0, column=2)


L3 = Label(root, text="Text to be Encrypted:", font = ('Arial',12))
E3 = Entry(root, bd=1)

R3 = Button(root, text="Select Image",  font = ('Arial',12), command=lambda: selectF(root))


R4 = Button(root, text="Encrypt Message",  font = ('Arial',12), command=lambda: runSt(L1, L2, L3, E1, E2, E3, R4, 1))


L1.grid(row=1)
E1.grid(row=1, column=1, columnspan=2)
L3.grid(row=2)
E3.grid(row=2, column=1, columnspan=2)
R3.grid(row=4, column=0, columnspan=3)
R4.grid(row=5, column=0, columnspan=3)

root.mainloop()
