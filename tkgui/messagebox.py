import tkinter as tk
# import tkinter.messagebox
from tkinter import messagebox 
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title="hi",message="hahahahahahahaha")
    # tk.messagebox.showinfo(title='Hi', message='hahahaha')
    #tk.messagebox.showwarning(title='Hi', message='nononono')
    #tk.messagebox.showerror(title='Hi', message='No!! never')
    #print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'
    #print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
    # print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))   # return True, False
    # print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
    # print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()