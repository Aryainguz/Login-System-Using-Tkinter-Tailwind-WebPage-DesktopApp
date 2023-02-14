from tkinter import *

root = Tk()

e = Entry(root,width=100)
e.grid(row=0,column=0)

def x(n):
    e.insert(0,n)

xi = Button(root,text='1',padx=40,pady=20,command=lambda: x(1))
xi.grid(row=1,column=0)


xii = Button(root,text='2',padx=40,pady=20,command=lambda: x(2))
xii.grid(row=1,column=1)

root.mainloop()
