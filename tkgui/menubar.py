import tkinter as tk

window=tk.Tk()
window.title("my eight python window GUI")
window.geometry("500x200")

l=tk.Label(window,text="do0",bg="orange",width=6)
l.pack()
counter=0
def do_job():
    global counter
    counter+=1
    l.config(text="do"+str(counter))

menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=1)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=do_job)
filemenu.add_command(label="open",command=do_job)
filemenu.add_command(label="save",command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)

editmenu=tk.Menu(menubar,tearoff=1)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)
editmenu.add_separator()
editmenu.add_command(label="Exit",command=window.quit)

submenu=tk.Menu(filemenu)
filemenu.add_cascade(labe="Import",menu=submenu,underline=1)
submenu.add_command(label="submenu1",command=do_job)


window.config(menu=menubar)
window.mainloop()