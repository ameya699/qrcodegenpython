from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image,ImageTk


root=Tk()
root.title("QR Code Generator")
root.iconbitmap('./static/applogo.jpg')
root.geometry('500x500')

def create_code():
    input_path=filedialog.asksaveasfilename(title="Save Image",filetypes=(("PNG File"),("All Files","*.*")))
    if input_path:
        if input_path.endswith(".png"):
            get_code=pyqrcode.create(my_entry.get())
            get_code.png(input_path,scale=5)
        else:
            input_path=f'{input_path}.png'
            get_code=pyqrcode.create(my_entry.get())
            get_code.png(input_path,scale=5)
        global get_image
        get_image=ImageTk.PhotoImage(Image.open(input_path))

        my_label.config(image=get_image)
        my_entry.delete(0,END)
        my_entry.insert(0,"Finished")

def clear_all():
    my_entry.delete(0,END)
    my_label.config(image='')

#creating ui
my_entry=Entry(root,font=('Helvetica',18))
my_entry.pack(pady=20)

my_button=Button(root,text="Create QR Code",command=create_code)
my_button.pack(pady=20)

my_button2=Button(root,text="Clear",command=clear_all)
my_button2.pack()

my_label=Label(root,text='')
my_label.pack(pady=20)

root.mainloop()
