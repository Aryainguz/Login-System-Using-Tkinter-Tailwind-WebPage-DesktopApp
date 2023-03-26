from tkinter import *
from tkinter import ttk
import ttkthemes
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import mpmath


def login():
    global eusernme
    global epassword
    if eusernme.get() == '' or epassword.get() == '':
        messagebox.showerror(
            'In a hurry ? (Error)', 'Fields can not be empty we made the application with a lot of time, take a lil to fill the details correctly')
    elif eusernme.get() in ['Ayush','Aryan','Arpit','Ayush'] or epassword.get() == '1416':
        messagebox.showinfo('Welcome Chitkarian ! ' , 'You will redirected to The Xiting World on clicking on ok')
        webbrowser.open('C:\Inguz\COLLECTION 1\project chitkara\index.html')
    else:
        messagebox.showerror('INVALID!', 'Please enter the correct details')
        
def admnlogin():
    root.destroy()
    import third

def exit():
    root.destroy()




root = ttkthemes.ThemedTk()
root.get_themes()    
root.set_theme('breeze') 



root.resizable(False, False)
root.iconbitmap( r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")
root.geometry('1200x628+150+30')
root.title('The Xiting Chitkara app by Aryan, Arpita Sambher, Aryan Gupta')


img = ImageTk.PhotoImage(file='C:\Inguz\logo.png')
alabel = ttk.Label(root, image=img)
alabel.place(x=0, y=0)


login_frame = ttk.Frame(root)
login_frame.place(x=350, y=100)

# for bigger image which tells to login
img2 = ImageTk.PhotoImage(
    file=r"C:\Inguz\pngtree-user-login-or-authenticate-icon-on-gray-background-flat-icon-ve-png-image_1786166.jpg")
username_label = ttk.Label(login_frame, image=img2)
username_label.grid(row=0, column=0, pady=0, padx=40)

# for username
img3 = ImageTk.PhotoImage(file=r"C:\Inguz\user-2935373__340.jpg")
username_label2 = Label(login_frame, image=img3, text='Username', compound=LEFT, font=('Helvetica', 20, 'bold'))
username_label2.grid(row=1, column=0, pady=5, padx=40)

# for password
img4 = ImageTk.PhotoImage(file=r"C:\Inguz\lock-4441691__340.png")
username_label3 = Label(login_frame, image=img4, text='Password',
                        compound=LEFT, font=('Helvetica', 20, 'bold'))
username_label3.grid(row=2, column=0, pady=5, padx=40)

# entries for username and password
eusernme = ttk.Entry(login_frame, width=30, font=('arial', 10, 'bold'))
epassword = ttk.Entry(login_frame, width=30, font=('arial', 10, 'bold'))

eusernme.grid(row=1, column=1, pady=5, padx=40)
epassword.grid(row=2, column=1, pady=5, padx=40)

# button for login
b1 = ttk.Button(root, text='login as administrator', command=admnlogin,width=20)
b1.place(x=1000, y=580,height=40)
b2 = ttk.Button(login_frame, text='login as Chitkararian', command=login)
b2.grid(row=3,column=1,padx=3,pady=20)
b3 = ttk.Button(root,text=' Exit ',command=exit)
b3.place(x=1100,y=10)

root.mainloop()
