from tkinter import *

window = Tk()
window.title("Product")
window.geometry("400x300")

lb1 = Label(text="Hi, there", fg="white", bg="blue", height=1, width=300)
lb2 = Label(text="Enter the first number", fg="white", bg="lightblue", height=1, width=100)
lb3 = Label(text="Enter the second number", fg="white", bg="lightblue", height=1, width=100)
inp1 = Entry()
inp2 = Entry()

def display():
  num1 = int(inp1.get())
  num2 = int(inp2.get())
  pro = num1*num2
  message = f"The product is {pro}"
  
  text_box.insert(END, message)
  
text_box = Text(height=1)

btn = Button(text="Submit", command=display, fg="white", bg="red", height=1)

lb1.pack()
lb2.pack()
inp1.pack()
lb3.pack()
inp2.pack()
btn.pack()
text_box.pack()

window.mainloop()