import tkinter as tk

window=tk.Tk()
window.title("first python window GUI")
window.geometry("500x500")

text=tk.StringVar()
l=tk.Label(window,height=2,width=20,bg="green",textvariable=text)
l.pack()

on_hit=False
def hit_fun():
    global on_hit
    if on_hit==False:
        on_hit=True
        text.set("hello world!")
    else:
        on_hit=False
        text.set("") 
b=tk.Button(window,text="hit me",width=10,height=2,bg="red",command=hit_fun)
b.pack()
window.mainloop()