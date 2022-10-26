from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

# TKINTER GUI APP -------------------------------------------------
root = Tk()
root.title(" Message Masker")
root.geometry("700x730+150+180")
root.resizable(False, False)
root.configure(bg="#fff791")


## FUNC SHOW IMAGE ------------------------------------------------
def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title = 'Select Image File',
        filetype = (("PNG File", "*.png"), ("JPG File", "*.jpg"), ("All File", "*.txt")))

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=585, height=395)
    lbl.image = img
    text1.delete(1.0, END)
    

## FUNC SAVE ------------------------------------------------------
def Save():
    global secret
    message = text1.get(1.0, END)

    if message == "\n":
        messagebox.showinfo("Message box", "No message detected!\nPlease add a message to continue.")
    else:
        secret = lsb.hide(str(filename), message)
        messagebox.showinfo("Message box", 'Your message was successfuly added!\n\nA new image named "hidden.png" was successfuly saved.\nPlease check your folder and rename the file.')
        saved_filename = filename.split(".")
        secret.save(f"{saved_filename[0]}(!).png")
        text1.delete(1.0, END)


## FUNC SHOW ------------------------------------------------------
def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


## FUNC CLEAR -----------------------------------------------------
def Clear():
    text1.delete(1.0, END)


## ICON -----------------------------------------------------------
image_icon = PhotoImage(file="icons/favicon.png")
root.iconphoto(False, image_icon)


## LOGO -----------------------------------------------------------
logo = PhotoImage(file="icons/logo.png")
Label(root, image=logo, bg="#fff791").place(x=45, y=10)

Label(root, text="SECRET MESSAGE", bg="#fff791", fg="#21201d", font="unispace 20 bold").place(x=128, y=50)


## FIRST FRAME ----------------------------------------------------
f = Canvas(root, bd=3, bg="#21201d", width=590, height=400, relief=GROOVE)
f.place(x=50, y=100)

lbl = Label(f, bg="black")
lbl.place(x=5, y=5)


## SECOND FRAME ---------------------------------------------------
Label(text="Enter your message below:", bg="#fff791", fg="#21201d", font="unisoft 9").place(x=50, y=530)

frame2 = Frame(root, bd=3, width=600, height=100, bg="#f2f2f2", relief=GROOVE)
frame2.place(x=50, y=550)

text1 = Text(frame2, font="Roboto 15", bg="#f2f2f2", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=580, height=95)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=576, y=0, height=93)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


## OPEN IMG BUTTON ------------------------------------------------
Button(text="Open Image", width=11, height=1, bg="#3cd5ea", font="unispace 8", command=showimage).place(x=560, y=74)

## HIDE MSG BTN ---------------------------------------------------
Button(text="Hide\nMessage", width=9, height=2, bg="#fd678a", font="unispace 8", command=Save).place(x=50, y=655)

## SHOW MSG BTN ---------------------------------------------------
Button(text="Show\nMessage", width=9, height=2, bg="#09ffa9", font="unispace 8", command=Show).place(x=130, y=655)

## CLEAR BUTTON ---------------------------------------------------
Button(text="Clear\nTextbox", width=9, height=2, bg="#3cd5ea", font="unispace 8", command=Clear).place(x=210, y=655)



root.mainloop()
