from tkinter import *

root = Tk()
root.title("Tkinter Basics")
root.geometry("400x500+100+20")
root.iconbitmap("computer.ico")



def press():
	print("Pressed")

btnimage = PhotoImage(file="buttonimage.png")
txtimage= PhotoImage(file="textimage.png")


text1 = Label(root,text="Hello world",fg="purple",font=("times new roman",20,"bold"))
text1.grid(row=0,column=0,padx=10,pady=20)

button1 = Button(root,text="Press me",fg="purple",bg="yellow",font=("times new roman",20,"bold"),command=press)
button1.grid(row=1,column=0)

text2 = Label(root,text="Hello world",image=txtimage,fg="purple",font=("times new roman",20,"bold"))
text2.grid(row=0,column=1)

button2 = Button(root,text="Press me",image=btnimage,fg="red",font=("times new roman",20,"bold"),command=press)
button2.grid(row=1,column=1)





root.mainloop()