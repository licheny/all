import tkinter as tk

window=tk.Tk()
window.title("third python window GUI")
window.geometry('200x300')

var1=tk.StringVar()
lb=tk.Label(window,bg="green",width=10,height=1,textvariable=var1)
lb.pack()

def select_point():
    value=lb.get(lb.curselection())
    var1.set(value)

b=tk.Button(window,width=10,height=1,command=select_point,text="select_point")
b.pack()

var2=tk.StringVar()
var2.set([11,22,33,44])
lb=tk.Listbox(window,listvariable=var2)
lb.pack()
item_list=["first","second","third","fourth"]
for i in item_list:
    lb.insert("end",i)
lb.insert(1,"hello")

window.mainloop()