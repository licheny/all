import tkinter as tk

window=tk.Tk()
window.title("my six python window GUI")
window.geometry("500x200")

l=tk.Label(window,bg="blue",width=20,text="empty")
l.pack()

var1=tk.IntVar()
var2=tk.IntVar()

def print_selection():
    if (var1.get()==1) & (var2.get()==1):
        # print(var1.get()==1)
        l.config(text="you select python and c++")
    elif (var1.get()==1) & (var2.get()==0):
        l.config(text="you select python")
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text="you select c++")
    else:
        l.config(text="empty")

c1=tk.Checkbutton(window,text="python",variable=var1,onvalue=1,offvalue=0,command=print_selection).pack()
c2=tk.Checkbutton(window,text="c++",variable=var2,onvalue=1,offvalue=0,command=print_selection).pack()
window.mainloop()