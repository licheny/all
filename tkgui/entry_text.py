import tkinter as tk

window=tk.Tk()
window.title("second windows GUI")
window.geometry("500x500")

e=tk.Entry(window)
e.pack()

def insert_point():
    var=e.get()
    t.insert("insert",var)

b1=tk.Button(window,width=20,height=2,bg="green",text="insert point",command=insert_point)
b1.pack()

def insert_end():
    var=e.get()
    t.insert("end",var)
    
b2=tk.Button(window,width=20,height=2,bg="red",text="insert end",command=insert_end)
b2.pack()

t=tk.Text(window,height=2)
t.pack()
window.mainloop()