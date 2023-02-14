from tkinter import *
from tkinter import ttk
import ttkthemes
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import mpmath

root3 = ttkthemes.ThemedTk()
root3.geometry('500x250+600+190')
root3.resizable(False, False)
root3.iconbitmap( r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")
root3.title('Enter Details as Administrator')

def  controlroomlogin():
    global eusernme
    global epassword
    if eusernme.get() in ['Aryainguz','aryainguz', 'ARYAINGUZ'] and epassword.get() == '369':
        messagebox.showinfo('Success!', 'Welcome Homie-:) ') 
        root3.destroy()
        import second 
    elif eusernme.get() in ['Arpita Sambher''arpita', 'Arpita'] and epassword.get() == '4100':
        messagebox.showinfo('Success!', 'Welcome Homie-:) ')
        root3.destroy()
        import second 
    elif eusernme.get() in ['Aryan Gupta', 'Aryan', 'aryan gupta'] and epassword.get() == '22003':
        messagebox.showinfo('Success!', 'Welcome Homie-:) ')
        root3.destroy()
        import second 
      

# for username

img3 = ImageTk.PhotoImage(file=r"C:\Inguz\user-2935373__340.jpg")
username_label2 = Label(root3, image=img3, text='Username',
                        compound=LEFT, font=('Helvetica', 20, 'bold'))
username_label2.grid(row=0, column=0, pady=3, padx=0)

# for password

img4 = ImageTk.PhotoImage(file=r"C:\Inguz\lock-4441691__340.png")
username_label3 = Label(root3, image=img4, text='Password',
                        compound=LEFT, font=('Helvetica', 20, 'bold'))
username_label3.grid(row=2, column=0, pady=3, padx=0)

# for entry of username

eusernme = ttk.Entry(root3,width=25,font=('arial', 10, 'bold'))
epassword = ttk.Entry(root3, width=25,font=('arial', 10, 'bold'))

eusernme.grid(row=0, column=1,pady=5, padx=40)
epassword.grid(row=2, column=1,pady=5, padx=40)

# button for login
bx = ttk.Button(root3, text='login to Control Room',width=25,command=controlroomlogin)
bx.place(x=300,y=200,height=30)




root3.mainloop()
