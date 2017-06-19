# import tkinter as tk

# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# var = tk.StringVar()
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()

# def print_selection():
#     l.config(text='you have selected ' + var.get())

# r1 = tk.Radiobutton(window, text='Option A',
#                     variable=var, value='A',
#                     command=print_selection)
# r1.pack()
# r2 = tk.Radiobutton(window, text='Option B',
#                     variable=var, value='B',
#                     command=print_selection)
# r2.pack()
# r3 = tk.Radiobutton(window, text='Option C',
#                     variable=var, value='C',
#                     command=print_selection)
# r3.pack()


# window.mainloop()

# print(True & True)

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()


window.mainloop()
