from tkinter import *

'''root = Tk() #Creates the box shaped widget
my_label = Label(root,text="Hello World!")#Creates a Label widget

#Put the label inside the box created:
#1) Pack Method: Shove the label inside the box (unsophisticated way)
my_label.pack()

root.mainloop() #Creates the main loop'''

'''root = Tk()
my_Label1 = Label(root, text = "Hello World!")
my_Label2 = Label(root, text = "My name is XYZ!")

#Put the label inside the box created:
#2) Grid Positioning System: rows and columns
my_Label1.grid(row=0,column=0)
my_Label2.grid(row=1,column=1)
#Note: my_Label2.grid(row=1,column=5) will look the same as my_Label2.grid(row=1,column=1) because there's nothing in columns 1 through 4; so, Tkinter will just ignore it.(same is true about rows)

root.mainloop()'''

'''#Creating Buttons
root = Tk()
def button():
    Label3= Label(root,text="Botton clicked!",fg="blue")
    Label3.pack()
my_button = Button(root,text = "Click Me!",padx=50,pady=50,command=button,fg="yellow",bg="black")
#fg: foreground color(text color),bg: background color,padx: length along x,pady: length along y,command:function called without()
my_button.pack()
root.mainloop()'''

'''#Creating Input Fields
root = Tk()
e = Entry(root,width=50) #Take input in a text box
e.pack()
def button():
    Label3= Label(root,text="Hello "+e.get())
    Label3.pack()
my_button = Button(root,text="Submit",command=button)
my_button.pack()
root.mainloop()'''

'''root = Tk()
e = Entry(root,width=50) #Take input in a text box
e.pack()
e.insert(0,"Enter the name...")
def button():
    Label3= Label(root,text="Hello "+e.get())
    Label3.pack()
my_button = Button(root,text="Submit",command=button)
my_button.pack()
root.mainloop()'''
