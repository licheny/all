import tkinter as tk

window=tk.Tk()
window.title("five window GUI")
window.geometry("200x300")

l=tk.Label(window,bg="orange",width=20,text="empty")
l.pack()

def print_selection():
    l.config(text="you select radio"+var.get())

var=tk.StringVar()
r1=tk.Radiobutton(window,text="Radio A",variable=var,value="A",command=print_selection)
r1.pack()

# var=tk.StringVar()
r2=tk.Radiobutton(window,text="Radio B",variable=var,value="B",command=print_selection)
r2.pack()

# var=tk.StringVar()
r3=tk.Radiobutton(window,text="Radio C",variable=var,value="C",command=print_selection)
r3.pack()

window.mainloop()