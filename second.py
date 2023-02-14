from tkinter import *
from tkinter import ttk # helps applying themes
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import ttkthemes
import math
import mpmath

root2 = ttkthemes.ThemedTk()  # ttkthemes.ThemedTk() works same as Tk() but with extra themes on buttons,etc

root2.get_themes()    
root2.set_theme('breeze')   # theme argumennt/name should be smaller


root2.title(' WELCOME ARYAINGUZ ! ')
root2.resizable(False, False)
root2.iconbitmap(r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")
root2.geometry('1200x700+150+30')

# Two variables that will make our text slider


def calc():
    messagebox.showwarning('Scientific Calculator!','Opening Scientific Calculator this will minimize the Control Room page as long as you do not exit calculator ! ')
    root2.destroy()
    import Zcalculator
    import second

def databaseLOGIN():
    global newe
    global newe2
    if newe.get()=='' or newe2.get() =='':
        messagebox.showerror(
            'OH NO!', 'Fields Can Not Be Empty')
    elif newe.get() in  ['369','4100','22003'] and newe2.get() in ['Aryainguz','aryainguz','aryan','Arpita','arpita'] :
        messagebox.showinfo('Success!', ' Connecting To Database')
    else:
        messagebox.showerror('I WARN YOU', 'You Have Entere The Wrong Password Retry To Convince Me You Are Have Access To Control Room')
    


def connectDATABASE():
    global newe
    global newe2
    newWINDOW =  Toplevel()        # Toplevel() is a class that creates a new window on top of existing user
    newWINDOW.geometry('470x200+730+230')
    newWINDOW.resizable(False,False)
    newWINDOW.title('Connect To Database')
    newWINDOW.iconbitmap(r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")


    newlabel2 = Label(newWINDOW, text='Enter Developer Name')
    newlabel = Label(newWINDOW,text='Enter Devloper Code')

    newe = Entry(newWINDOW,font=('roman',15,'bold'),bd=2)
    newe2 = Entry(newWINDOW,font=('roman',15,'bold'),bd=2)

    newBTN = ttk.Button(newWINDOW,text='Connect To Database',command=databaseLOGIN)

    newlabel.grid(row=0,column=0,padx=40,pady=20)
    newlabel2.grid(row=2,column=0,padx=40,pady=20)

    newe.grid(row=0,column=1,padx=40,pady=20)
    newe2.grid(row=2,column=1,padx=40,pady=20)

    newBTN.grid(row=4,column=1,padx=40,pady=20)

def clock():
    date = time.strftime('%d-%m-%Y')  # this gives date and time in formatedform
    currentTime = time.strftime('%H:%M:%S')
    lablea.config(text=f'    Date : {date}\nTime : {currentTime}')  # config() method helps to update data , information,etc
    lablea.after(1000,clock)    # this helps update data after specified time here LHS argument is time in milli seconds i.e after 1000 milliseconds or 1 second data will update and RHS argument is function to be updated


# use ttk. eg-: ttk.label(), ttk.Entry(), ttk.Button(),etc where ever you want to apply the theme 
lablea = Label(root2,font=('Helvetica',13))
lablea.place(x=0,y=630)
clock()  # write clock here otherwise funct. won't work

labelc = ttk.Label(root2,text='THE CONTROL ROOM',font=('roman',30,'italic bold') )
labelc.place(x=20,y=20)

s= ImageTk.PhotoImage(file=r"C:\Inguz\28-11-2022 12_33_14 AM.png")
labelb = ttk.Label(root2,image=s,font=('arial',20,'italic bold'))
labelb.place(x=20,y=80)

# left side

leftframe = Frame(root2)  
leftframe.place(x=20,y=300,width=300,height=300)

# imgc = PhotoImage(file=r'C:\Inguz\28-11-2022 12_33_14 AM.png')
# labelc = Label(leftframe,image=imgc)
# labelc.grid(row=0,column=0)

BtnA = ttk.Button(root2,text='Add a user',width=25)
BtnA.place(x=50,y=270)

BtnB = ttk.Button(root2,text='Search a user',width=25)
BtnB.place(x=50,y=320)

BtnC = ttk.Button(root2,text='Delete a user',width=25)
BtnC.place(x=50,y=370)

BtnD = ttk.Button(root2,text='Update a user',width=25)
BtnD.place(x=50,y=420)


BtnE = ttk.Button(root2,text='Export Data',width=25)
BtnE.place(x=50,y=470)

btnZ = ttk.Button(root2,text='Connect to Database',command=connectDATABASE)  
btnZ.place(x=1030,y=620)

btnB = ttk.Button(root2,text='Get a Calculator',command=calc,width=17)
btnB.place(x=1030,y=660)

# right side

rightframe = Frame(root2)
rightframe.place(x=380,y=30,width=650,height=600)

# treeview is used for preview of database it is only for ttk tkinter it does not work for tk()


# if you don't write orient by default it will be Horizontal

scroll1 = Scrollbar(rightframe,orient=HORIZONTAL)
scroll2 = Scrollbar(rightframe,orient=VERTICAL)


scroll1.pack(side=BOTTOM,fill=X)
scroll2.pack(side=RIGHT,fill=Y)

studentTable = ttk.Treeview(rightframe,columns=('ID','Name','Mobile No.','Email id','The Xiting Score','The Zero score'),xscrollcommand=scroll1.set,yscrollcommand=scroll2.set)
studentTable.pack(fill=BOTH,expand=1)  # fill = both fills x and y and epand = 1 expands it to frame completely

# this tells scroll bar to mave window in x direction

scroll1.config(command=studentTable.xview)
scroll2.config(command=studentTable.yview)

# Now working in table
studentTable.heading('ID',text='ID')
studentTable.heading('Name',text='NAME')
studentTable.heading('Mobile No.',text='Mobile No.')
studentTable.heading('Email id',text='Email id')
studentTable.heading('The Xiting Score',text='The Xiting Score')
studentTable.heading('The Zero score',text='The Zero score')


root2.mainloop()